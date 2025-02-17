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

    def test_is_identical(self):
        self.assertTrue(
            textnode.TextNode("text", textnode.TextType.NORMAL, "url").is_identical(
                textnode.TextNode("text", textnode.TextType.NORMAL, "url")
            )
        )

    def test_is_not_identical(self):
        self.assertFalse(
            textnode.TextNode("text", textnode.TextType.NORMAL, "url").is_identical(
                textnode.TextNode("text", textnode.TextType.NORMAL, None)
            )
        )

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
        self.assertEqual(node1.__repr__(), f"TextNode({"\"This is a text node\""}, {textnode.TextType.BOLD}, {"http://example.org"})")

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
                         
    def test_split_nodes_delimiter_valid_bold_middle_returns_correct_amount(self):
        node = textnode.TextNode("This is an **bolded** node", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)

    def test_split_nodes_delimiter_valid_italic_middle_returns_correct_amount(self):
        node = textnode.TextNode("This is an *italicized* node", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "*", textnode.TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)

    def test_split_nodes_delimiter_valid_code_middle_returns_correct_amount(self):
        node = textnode.TextNode("This is an `code` node", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "`", textnode.TextType.CODE)
        self.assertEqual(len(new_nodes), 3)

    def test_split_nodes_delimiter_valid_full_text_bolded(self):
        node = textnode.TextNode("**This is a bolded node**", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.TextType.BOLD)
        with self.subTest():
            self.assertEqual(len(new_nodes), 1)
        with self.subTest():
            self.assertTrue(new_nodes[0].is_identical(textnode.TextNode("This is a bolded node", textnode.TextType.BOLD)))

    def test_split_nodes_delimiter_multi_valid_bold_middle_returns_correct_amount(self):
        node = textnode.TextNode("This **is** an **bolded** node", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.TextType.BOLD)
        self.assertEqual(len(new_nodes), 5)

    def test_split_nodes_delimiter_no_delim_found(self):
        node = textnode.TextNode("This is an bolded node", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "**", textnode.TextType.BOLD)
        self.assertEqual(node, new_nodes[0])

    def test_split_nodes_delimiter_delim_no_match(self):
        node = textnode.TextNode("This is *an** bolded node", textnode.TextType.NORMAL)
        with self.assertRaises(TypeError):
            textnode.split_nodes_delimiter(
                [node],
                "*",
                textnode.TextType.ITALIC
            )

    def test_split_nodes_delimiter_delim_at_front(self):
        node = textnode.TextNode("*This* is an italicized node", textnode.TextType.NORMAL)
        new_nodes = textnode.split_nodes_delimiter([node], "*", text_type=textnode.TextType.ITALIC)
        with self.subTest():
            self.assertEqual(len(new_nodes), 2)
        with self.subTest():
            self.assertEqual(
                new_nodes[0],
                textnode.TextNode("This", textnode.TextType.ITALIC)
            )
        with self.subTest():
            self.assertEqual(
                new_nodes[0].text,
                "This"
            )
        with self.subTest():
            self.assertEqual(
                new_nodes[1],
                textnode.TextNode(" is an italicized node", textnode.TextType.NORMAL)
            )
        with self.subTest():
            self.assertEqual(
                new_nodes[1].text,
                " is an italicized node"
            )

    def test_split_nodes_delimiter_delim_at_end(self):
        node = textnode.TextNode("This is an italicized *node*")
        new_nodes = textnode.split_nodes_delimiter([node], "*", text_type=textnode.TextType.ITALIC)
        with self.subTest():
            self.assertEqual(len(new_nodes), 2)
        with self.subTest():
            self.assertEqual(
                new_nodes[0],
                textnode.TextNode("This is an italicized ", textnode.TextType.NORMAL)
            )
        with self.subTest():
            self.assertEqual(
                new_nodes[0].text,
                "This is an italicized "
            )
        with self.subTest():
            self.assertEqual(
                new_nodes[1],
                textnode.TextNode("node", textnode.TextType.ITALIC)
            )
        with self.subTest():
            self.assertEqual(
                new_nodes[1].text,
                "node"
            ) 
            
    def test_split_node_delimiter_multiple_nodes(self):
        txt_node = textnode.TextNode("This is a text node")
        ital_node = textnode.TextNode("This is an *italicized* node")
        bold_node = textnode.TextNode("This is a **bolded** node")
        code_node = textnode.TextNode("This is a `code` node")

        nodes = [txt_node, ital_node, bold_node, code_node]
        new_nodes = textnode.split_nodes_delimiter(nodes, "**", textnode.TextType.BOLD)
        new_nodes = textnode.split_nodes_delimiter(new_nodes, "*", textnode.TextType.ITALIC)
        new_nodes = textnode.split_nodes_delimiter(new_nodes, "`", textnode.TextType.CODE)

        print(f"\ntest_split_node_delimiter\n.......................\n{new_nodes}")
        self.assertEqual(len(new_nodes),  10)
        
    def test_extract_markdown_images_single_link(self):
        txt_node = textnode.TextNode("This is text with a ![alt text](http://example.org).")
        print(f"\ntest_extract_markdown_images_single_link\n.......................\n{txt_node.extract_markdown_images()}\n")
        self.assertEqual(
            txt_node.extract_markdown_images(),
            [("alt text", "http://example.org")]
        )
        

    def test_extract_markdown_images_multiple_links(self):
        txt_node = textnode.TextNode("This is ![alt text](http://example.org) text with a ![alt text 2](http://example.org/2).")
        print(f"\ntest_extract_markdown_images_multiple_links\n.......................\n{txt_node.extract_markdown_images()}\n")
        self.assertEqual(
            txt_node.extract_markdown_images(),
            [("alt text", "http://example.org"), ("alt text 2", "http://example.org/2")]
        )
        
    def test_extract_markdown_images_bad_link(self):
        txt_node = textnode.TextNode("This is text with a ![alt text 2(http://example.org/2).")
        print(f"\ntest_extract_markdown_images_bad_link\n.......................\n{txt_node.extract_markdown_images()}\n")
        self.assertEqual(
            txt_node.extract_markdown_images(),
            []
        )

    def test_extract_markdown_links_single_link(self):
        txt_node = textnode.TextNode("This is text with a [text](http://example.org).")
        print(f"\ntest_extract_markdown_links_single_link\n.......................\n{txt_node.extract_markdown_links()}\n")
        self.assertEqual(
            txt_node.extract_markdown_links(),
            [("text", "http://example.org")]
        )
        

    def test_extract_markdown_links_multiple_links(self):
        txt_node = textnode.TextNode("This is [alt text](http://example.org) text with a [alt text 2](http://example.org/2).")
        print(f"\ntest_extract_markdown_images_multiple_links\n.......................\n{txt_node.extract_markdown_links()}\n")
        self.assertEqual(
            txt_node.extract_markdown_links(),
            [("alt text", "http://example.org"), ("alt text 2", "http://example.org/2")]
        )

    def test_extract_markdown_link_bad_link(self):
        txt_node = textnode.TextNode("This is text with a alt text 2](http://example.org/2).")
        print(f"\ntest_extract_markdown_images_bad_link\n.......................\n{txt_node.extract_markdown_links()}\n")
        self.assertEqual(
            txt_node.extract_markdown_links(),
            []
        )

if __name__ == "__main__":
    unittest.main(verbosity = 2)