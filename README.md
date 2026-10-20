# Translations

One language control for every app. Pick English, Espanol, Francais or Deutsch once here, and every supported app on the Pi speaks that language - menus, HUDs, pause and game-over screens, help lines.

All translations live in this app's catalog (`catalog.py`), hand-written and reviewed, no network, no APIs, no keys. Apps never translate themselves: they read the shared store this app owns at `~/pi-translations/` through a tiny embedded loader (`pi18n.py`). With no store present, every app simply runs in English, so every app still works zero-setup.

Currently covers: girderdash, cranestack, arcadewisp, blockboa, flingfort, flipspire, snake-arena, and this app itself. More apps join as they are updated.

## Run

```
python3 translations.py
```

Python 3 with curses. No dependencies, no network, no install.

## Controls

- **Up/Down (or w/s)** - choose a language
- **Enter** - apply it to all apps (writes `~/pi-translations/language` + one pack per app)
- **R** - reset everything to English
- **Q** - quit

## How apps join

Each app ships a copy of `pi18n.py` and asks it for its strings:

```python
import pi18n
S = pi18n.load("myapp", DEFAULT_STRINGS)   # English defaults stay in the app
```

The Translations app writes `~/pi-translations/myapp.json` from its catalog; the loader overlays that pack onto the defaults when the current language matches. Only this app writes the store.

## Tests

```
python3 -m unittest test_translations
```

14 tests: catalog key/placeholder coverage across all languages, pack writing, loader fallback and overlay behavior, reset, render rows, and a real terminal (PTY) boot-apply-quit run.

Built with AI assistance from my design.
