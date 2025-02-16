import unittest
import leafnode

class TestLeafNode(unittest.TestCase):

    def test_valid_leafnode_no_props(self):
        l = leafnode.LeafNode("p", "This is a paragraph.")
        self.assertEqual(l.to_html(), f"<p>This is a paragraph.</p>")

    def test_valid_leafnode_with_props(self):
        l = leafnode.LeafNode("a", "This is a link.", {"href": "https://example.org"})
        self.assertEqual(l.to_html(), f"<a href=\"https://example.org\">This is a link.</a>")

    def test_leafnode_create_with_empty_value(self):
        self.assertRaises(ValueError, leafnode.LeafNode, value = None)

    def test_leafnode_to_html_with_empty_value(self):
        l = leafnode.LeafNode("p", "value")
        l.value = None
        self.assertRaises(ValueError, l.to_html)
