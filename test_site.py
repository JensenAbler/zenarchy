import pathlib
import unittest

class SiteTests(unittest.TestCase):
    def test_document_and_stylesheet(self):
        page = pathlib.Path(__file__).with_name("index.html").read_text()
        self.assertIn("<!doctype html>", page.lower())
        self.assertIn("style.css", page)
        self.assertTrue(pathlib.Path(__file__).with_name("style.css").is_file())
