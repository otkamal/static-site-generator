import unittest
import textnode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node1 = textnode.TextNode("This is a text node", textnode.TextType.BOLD)
        node2 = textnode.TextNode("This is a test node", textnode.TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_text_nq(self):
        node1 = textnode.TextNode("Text 1", textnode.TextType.BOLD)
        node2 = textnode.TextNode("Text 2", textnode.TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_type_nq(self):
        node1 = textnode.TextNode("This is a text node", textnode.TextType.ITALIC)
        node2 = textnode.TextNode("This is a test node", textnode.TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_eq(self):
        node1 = textnode.TextNode("This is a text node", textnode.TextType.BOLD, "http://example.org")
        node2 = textnode.TextNode("This is a test node", textnode.TextType.BOLD, "http://example.org")
        self.assertEqual(node1, node2)

    def test_url_nq(self):
        node1 = textnode.TextNode("This is a text node", textnode.TextType.BOLD, "hello world")
        node2 = textnode.TextNode("This is a test node", textnode.TextType.BOLD, "http://example.org")
        self.assertEqual(node1, node2)

    def test_unset_url(self):
        node1 = textnode.TextNode("This is a text node", textnode.TextType.BOLD)
        node2 = textnode.TextNode("This is a test node", textnode.TextType.BOLD, "http://example.org")
        self.assertEqual(node1, node2)

    def test_print(self):
        node1 = textnode.TextNode("This is a text node", textnode.TextType.BOLD, "http://example.org")
        self.assertEqual(node1.__repr__(), f"TextNode({"This is a text node"}, {textnode.TextType.BOLD}, {"http://example.org"})")

if __name__ == "__main__":
    unittest.main()