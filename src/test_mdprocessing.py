import unittest
import mdprocessing

class TestMdProcessing(unittest.TestCase):
    def test_markdown_to_blocks_three_valid_blocks(self):
        markdown = '''# This is a heading

                    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                    * This is the first list item in a list block\n* This is a list item\n* This is another list item'''
        expecting = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(mdprocessing.markdown_to_blocks(markdown), expecting)


    def test_markdown_to_blocks_one_block(self):
        markdown = "This is a single block"
        expecting = ["This is a single block"]
        self.assertEqual(mdprocessing.markdown_to_blocks(markdown), expecting)

    def test_markdown_to_blocks_remove_trailing_new_lines(self):
        markdown = "This is a single block\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        expecting = ["This is a single block"]
        self.assertEqual(mdprocessing.markdown_to_blocks(markdown), expecting)

    def test_markdown_to_blocks_excessive_new_lines(self):
        markdown = "This is a single block\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis is a second block"
        expecting = ["This is a single block", "This is a second block"]
        self.assertEqual(mdprocessing.markdown_to_blocks(markdown), expecting)

    def test_markdown_to_blocks_trim_whitespace(self):
        markdown = "                 This is a single block \n\n  This is a second block                 "
        expecting = ["This is a single block", "This is a second block"]
        self.assertEqual(mdprocessing.markdown_to_blocks(markdown), expecting)