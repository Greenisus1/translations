import json, os, sys, tempfile, unittest
from unittest import mock
from pathlib import Path
sys.path.insert(0, '/tmp/translations-pkg')
import catalog, pi18n, translations as tr

class CatalogTests(unittest.TestCase):
    def test_every_language_covers_every_key(self):
        for app, d in catalog.APPS.items():
            keys = set(d["strings"])
            for lang in catalog.LANGS:
                if lang == "en": continue
                self.assertIn(lang, d, (app, lang))
                self.assertEqual(set(d[lang]), keys, (app, lang))
    def test_format_placeholders_preserved(self):
        import re
        for app, d in catalog.APPS.items():
            for key, en in d["strings"].items():
                want = set(re.findall(r"{(\w+)}", en))
                for lang in catalog.LANGS[1:]:
                    got = set(re.findall(r"{(\w+)}", d[lang][key]))
                    self.assertEqual(want, got, (app, key, lang))
    def test_no_empty_strings(self):
        for app, d in catalog.APPS.items():
            for lang in ["strings"] + catalog.LANGS[1:]:
                for k, v in d[lang].items():
                    self.assertTrue(v.strip(), (app, lang, k))

class PackTests(unittest.TestCase):
    def test_apply_writes_marker_and_packs(self):
        with tempfile.TemporaryDirectory() as d:
            n = tr.apply_language("es", d)
            self.assertEqual(n, len(catalog.APPS))
            self.assertEqual(open(os.path.join(d, "language")).read().strip(), "es")
            pack = json.load(open(os.path.join(d, "girderdash.json")))
            self.assertEqual(pack["lang"], "es")
            self.assertEqual(set(pack["strings"]), set(catalog.APPS["girderdash"]["strings"]))
    def test_apply_unknown_language_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertRaises(ValueError, tr.apply_language, "xx", d)
    def test_loader_uses_pack(self):
        with tempfile.TemporaryDirectory() as d:
            tr.apply_language("de", d)
            with mock.patch.object(pi18n, "DIR", d):
                S = pi18n.load("girderdash", catalog.APPS["girderdash"]["strings"])
                self.assertEqual(S["OUCH"], " AUTSCH! ")
    def test_loader_falls_back_to_english(self):
        with tempfile.TemporaryDirectory() as d:
            with mock.patch.object(pi18n, "DIR", d):
                S = pi18n.load("girderdash", catalog.APPS["girderdash"]["strings"])
                self.assertEqual(S["OUCH"], " OUCH! ")
    def test_loader_ignores_wrong_language_pack(self):
        with tempfile.TemporaryDirectory() as d:
            tr.apply_language("fr", d)
            os.remove(os.path.join(d, "language"))
            with mock.patch.object(pi18n, "DIR", d):
                S = pi18n.load("girderdash", catalog.APPS["girderdash"]["strings"])
                self.assertEqual(S["OUCH"], " OUCH! ")
    def test_loader_ignores_unknown_keys(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "language"), "w") as fh: fh.write("es")
            with open(os.path.join(d, "girderdash.json"), "w") as fh:
                json.dump({"lang": "es", "strings": {"NOPE": "x", "OUCH": " ¡AY! "}}, fh)
            with mock.patch.object(pi18n, "DIR", d):
                S = pi18n.load("girderdash", catalog.APPS["girderdash"]["strings"])
                self.assertNotIn("NOPE", S)
                self.assertEqual(S["OUCH"], " ¡AY! ")
    def test_reset_removes_everything(self):
        with tempfile.TemporaryDirectory() as d:
            tr.apply_language("es", d)
            n = tr.reset(d)
            self.assertGreaterEqual(n, 2)
            self.assertFalse(os.path.exists(os.path.join(d, "language")))
            self.assertFalse(os.path.exists(os.path.join(d, "girderdash.json")))
    def test_apply_en_resets(self):
        with tempfile.TemporaryDirectory() as d:
            tr.apply_language("es", d)
            tr.apply_language("en", d)
            self.assertFalse(os.path.exists(os.path.join(d, "language")))
    def test_installed_apps(self):
        with tempfile.TemporaryDirectory() as d:
            tr.apply_language("es", d)
            with mock.patch.object(pi18n, "DIR", d):
                got = tr.installed_apps(d)
                self.assertEqual(set(got), set(catalog.APPS))
    def test_render_rows(self):
        S = catalog.APPS["translations"]["strings"]
        cells = tr.render(1, "msg", 80, 24, S)
        text = "\n".join(c[2] for c in cells)
        self.assertIn("TRANSLATIONS", text)
        self.assertIn("Espanol", text)
        self.assertIn("girderdash", text)

if __name__ == "__main__":
    unittest.main()


class PtyTests(unittest.TestCase):
    def spawn(self, d):
        import pty, subprocess
        master, slave = pty.openpty()
        env = dict(os.environ, TERM="xterm-256color", LINES="30", COLUMNS="90", PI18N_DIR=d)
        p = subprocess.Popen([sys.executable, "/tmp/translations-pkg/translations.py"],
                             stdin=slave, stdout=slave, stderr=slave, env=env, close_fds=True)
        os.close(slave)
        return p, master, bytearray()

    def drain(self, master, buf, until, timeout=8.0):
        import select, time
        end = time.time() + timeout
        while time.time() < end:
            r, _, _ = select.select([master], [], [], 0.1)
            if r:
                try: buf.extend(os.read(master, 65536))
                except OSError: break
                if until and until in bytes(buf): return True
        return bool(until and until in bytes(buf))

    def test_boot_apply_quit(self):
        with tempfile.TemporaryDirectory() as d:
            p, m, buf = self.spawn(d)
            try:
                self.assertTrue(self.drain(m, buf, b"TRANSLATIONS"), bytes(buf)[-300:])
                os.write(m, b"s\n")          # down to Espanol, enter
                self.assertTrue(self.drain(m, buf, "aplicado".encode()), bytes(buf)[-300:])
                self.assertEqual(open(os.path.join(d, "language")).read().strip(), "es")
                self.assertTrue(os.path.exists(os.path.join(d, "girderdash.json")))
                os.write(m, b"q")
                p.wait(timeout=5)
                self.assertEqual(p.returncode, 0)
            finally:
                if p.poll() is None: p.kill()
                os.close(m)
