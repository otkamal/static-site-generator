import unittest
from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_valid_h1(self):
        md = "# Header 1"
        self.assertEqual(extract_title(md), "Header 1")

    def test_valid_h1_with_whitespace(self):
        md = "                  #             Header 1                  "
        self.assertEqual(extract_title(md), "Header 1")
    
    def test_no_h1(self):
        with self.assertRaises(TypeError):
            extract_title("## Header 2")