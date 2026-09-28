import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).parent


class SiteTests(unittest.TestCase):
    def test_page_loads_its_assets(self):
        page = (ROOT / "index.html").read_text()
        self.assertIn("<!doctype html>", page.lower())
        for asset in ("style.css", "glyphs.js", "/portfolio-controls.js"):
            self.assertIn(asset, page)
        self.assertTrue((ROOT / "style.css").is_file())

    def test_every_referenced_glyph_exists(self):
        page = (ROOT / "index.html").read_text()
        src = (ROOT / "glyphs.js").read_text()
        glyphs = json.loads(src.split("window.GLYPHS=", 1)[1].strip().rstrip(";"))
        used = set(re.findall(r"img\(s,'([A-Za-z_]+?)(?:_n)?'", page)) | {"title"}
        self.assertTrue(used)
        self.assertFalse(used - set(glyphs), f"missing glyphs: {used - set(glyphs)}")


if __name__ == "__main__":
    unittest.main()
