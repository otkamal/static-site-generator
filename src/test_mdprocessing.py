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

    def test_block_to_blocktype_heading(self):
        text = "# heading 1"
        self.assertEqual(mdprocessing.block_to_BlockType(text), mdprocessing.BlockType.HEADING)

    def test_block_to_blocktype_code(self):
        text = "```This some code```"
        self.assertEqual(mdprocessing.block_to_BlockType(text), mdprocessing.BlockType.CODE)

    def test_block_to_blocktype_quote(self):
        text = "> This is a quote"
        self.assertEqual(mdprocessing.block_to_BlockType(text), mdprocessing.BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list(self):
        text = "* item 1\n* item 2\n* item 3"
        self.assertEqual(mdprocessing.block_to_BlockType(text), mdprocessing.BlockType.UNORDERED_LIST)

    def test_block_to_blocktype_ordered_list(self):
        text = "1. item 1\n2. item 2\n3. item 3"
        self.assertEqual(mdprocessing.block_to_BlockType(text), mdprocessing.BlockType.ORDERED_LIST)