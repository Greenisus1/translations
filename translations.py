#!/usr/bin/env python3
"""translations - one language control for every Greenisus1 Pi app.

Pick a language once here and every supported app speaks it. This app owns the
shared store at ~/pi-translations/: it writes the current language and one
string pack per app. Apps read that store at startup through their pi18n
loader; with no store present they run in English as usual.

An original app. Built with AI assistance from my design.
MIT License - Copyright (c) 2026 Greenisus1
"""
import curses, json, os, time

VERSION = "1.0.0"

import pi18n, catalog

DIR = pi18n.DIR

# ---------- pack writing (pure, unit-testable) ----------

def apply_language(lang, dest=None):
    dest = dest or pi18n.DIR
    """Write the language marker and one pack per catalog app. Returns app count."""
    if lang not in catalog.LANGS:
        raise ValueError("unknown language: " + lang)
    os.makedirs(dest, exist_ok=True)
    n = 0
    if lang == "en":
        reset(dest)
        return len(catalog.APPS)
    with open(os.path.join(dest, "language"), "w") as fh:
        fh.write(lang + "\n")
    for app, d in catalog.APPS.items():
        pack = {"lang": lang, "strings": d[lang]}
        with open(os.path.join(dest, app + ".json"), "w") as fh:
            json.dump(pack, fh, ensure_ascii=False, indent=1)
        n += 1
    return n

def reset(dest=None):
    dest = dest or pi18n.DIR
    """Back to English everywhere: remove the marker and every pack."""
    n = 0
    for name in ("language",):
        try: os.remove(os.path.join(dest, name)); n += 1
        except OSError: pass
    for app in catalog.APPS:
        try: os.remove(os.path.join(dest, app + ".json")); n += 1
        except OSError: pass
    return n

def installed_apps(dest=None):
    dest = dest or pi18n.DIR
    """Apps that currently have a pack for the current language."""
    lang = pi18n.current_language()
    out = []
    for app in catalog.APPS:
        try:
            with open(os.path.join(dest, app + ".json")) as fh:
                if json.load(fh).get("lang") == lang:
                    out.append(app)
        except (OSError, ValueError):
            pass
    return out

# ---------- UI ----------
C_TITLE, C_TEXT, C_HI, C_DIM, C_OK = range(1, 6)

def render(sel, message, W, H, S):
    """Pure grid render: returns list of (y, x, text, color)."""
    cells = []
    def t(y, x, s, k): cells.append((y, x, s, k))
    t(0, 2, S["TITLE"], C_TITLE)
    t(1, 2, S["CURRENT"].format(lang=catalog.LANG_NAMES[pi18n.current_language()]), C_TEXT)
    t(3, 2, S["PICK_LANG"], C_TEXT)
    for i, lang in enumerate(catalog.LANGS):
        name = catalog.LANG_NAMES[lang]
        mark = "█ " if i == sel else "  "
        cur = " <--" if lang == pi18n.current_language() else ""
        t(4 + i, 4, mark + name + cur, C_HI if i == sel else C_TEXT)
    row = 5 + len(catalog.LANGS)
    t(row, 2, S["APPS_HDR"], C_TEXT)
    apps = sorted(catalog.APPS)
    for i, app in enumerate(apps):
        n = len(catalog.APPS[app]["strings"])
        t(row + 1 + i, 4, f"{app} ({n})", C_DIM)
    if message:
        t(row + 2 + len(apps), 2, message, C_OK)
    t(H - 1, 2, S["APPLY"] + "   " + S["RESET"], C_DIM)
    return cells

def run(stdscr):
    curses.start_color(); curses.use_default_colors()
    curses.init_pair(C_TITLE, curses.COLOR_MAGENTA, -1)
    curses.init_pair(C_TEXT, curses.COLOR_WHITE, -1)
    curses.init_pair(C_HI, curses.COLOR_CYAN, -1)
    curses.init_pair(C_DIM, 8 if curses.COLORS > 8 else curses.COLOR_WHITE, -1)
    curses.init_pair(C_OK, curses.COLOR_GREEN, -1)
    curses.curs_set(0)
    sel = 0
    message = ""
    msg_until = 0.0
    while True:
        S = pi18n.load("translations", catalog.APPS["translations"]["strings"])
        H, W = stdscr.getmaxyx()
        if time.time() > msg_until: message = ""
        stdscr.erase()
        for y, x, s, k in render(sel, message, W, H, S):
            if 0 <= y < H and 0 <= x < W - 1:
                try: stdscr.addstr(y, x, s[:W - x - 1], curses.color_pair(k))
                except curses.error: pass
        stdscr.refresh()
        k = stdscr.getch()
        if k in (ord("q"), ord("Q")): return
        if k in (curses.KEY_UP, ord("w")): sel = (sel - 1) % len(catalog.LANGS)
        elif k in (curses.KEY_DOWN, ord("s")): sel = (sel + 1) % len(catalog.LANGS)
        elif k in (ord("r"), ord("R")):
            reset()
            message, msg_until = S["RESET_DONE"], time.time() + 3
        elif k in (10, 13, curses.KEY_ENTER):
            n = apply_language(catalog.LANGS[sel])
            S = pi18n.load("translations", catalog.APPS["translations"]["strings"])
            message = S["APPLIED"].format(lang=catalog.LANG_NAMES[catalog.LANGS[sel]], n=n)
            msg_until = time.time() + 3

def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()
