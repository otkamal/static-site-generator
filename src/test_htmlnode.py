import unittest
import htmlnode

class TestHTMLNode(unittest.TestCase):
    def test_creates_valid_html_property_string(self):
        node = htmlnode.HTMLNode(props = {"href":"http://example.org", "target":"_blank"})
        self.assertEqual(node.props_to_html(), " href=\"http://example.org\" target=\"_blank\"")

    def test_props_is_empty(self):
        node = htmlnode.HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_not_dictionary(self):
        self.assertRaises(TypeError, htmlnode.HTMLNode, props = 5)

    def test_to_html_not_implemented(self):
        self.assertRaises(NotImplementedError, htmlnode.HTMLNode().to_html)
