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

    def test_textnode_to_htmlnode_normal(self):
        node = textnode.TextNode("This is a text node", textnode.TextType.NORMAL)
        self.assertEqual(node.to_HTMLNode().to_html(), "This is a text node")

    def test_textnode_to_htmlnode_italic(self):
        node = textnode.TextNode("This is a italic node", textnode.TextType.ITALIC)
        self.assertEqual(node.to_HTMLNode().to_html(), "<i>This is a italic node</i>")

    def test_textnode_to_htmlnode_bold(self):
        node = textnode.TextNode("This is a bold node", textnode.TextType.BOLD)
        self.assertEqual(node.to_HTMLNode().to_html(), "<b>This is a bold node</b>")

    def test_textnode_to_htmlnode_code(self):
        node = textnode.TextNode("This is a code node", textnode.TextType.CODE)
        self.assertEqual(node.to_HTMLNode().to_html(), "<code>This is a code node</code>")

    def test_textnode_to_htmlnode_link(self):
        node = textnode.TextNode("This is a link node", textnode.TextType.LINK, "http://example.org")
        self.assertEqual(node.to_HTMLNode().to_html(), "<a href=\"http://example.org\">This is a link node</a>")

    def test_textnode_to_htmlnode_normal(self):
        node = textnode.TextNode("This is an image node", textnode.TextType.IMAGE, "http://example.org")
        self.assertEqual(node.to_HTMLNode().to_html(), "<img src=\"http://example.org\" alt=\"This is an image node\"></img>")
                         
if __name__ == "__main__":
    unittest.main(verbosity = 2)