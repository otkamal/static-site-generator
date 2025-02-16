import textnode
import htmlnode
import parentnode
from leafnode import LeafNode

def main():
    test = textnode.TextNode("test node", textnode.TextType.BOLD, "https://google.com")
    test2 = htmlnode.HTMLNode("a", "hello", [htmlnode.HTMLNode(), htmlnode.HTMLNode()])
    node = parentnode.ParentNode(
    "p",
    [
        parentnode.ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    print(node.to_html())

if __name__ == "__main__":
    main()