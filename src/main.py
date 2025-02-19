import textnode
import htmlnode
import parentnode
import mdprocessing
from leafnode import LeafNode

def main():
    # test = textnode.TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) [rick roll](https://i.imgur.com/aKaOqIh.gif) and more text [another link](https://i.imgur.com/aKaOqIh.gif) and more text", textnode.TextType.NORMAL)
    # print(textnode.split_nodes_link([test]))
    test = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    test_nodes = textnode.markdown_to_TextNodes(test)
    textnode.print_TextNodes(test_nodes)

    test_md = '''* item 1
    * Item 2'''
    print(mdprocessing.block_to_BlockType(test_md))

if __name__ == "__main__":
    main()