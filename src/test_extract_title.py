import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_one(self):
        heading = "# This is a heading!"
        proper_heading = "This is a heading!"
        attempt = extract_title(heading)
        self.assertEqual(attempt, proper_heading)

    def test_two(self):
        improper_markdown = "## This is a heading!"
        with self.assertRaises(Exception):
            extract_title(improper_markdown)
