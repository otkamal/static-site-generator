import textnode
import htmlnode
import parentnode
from leafnode import LeafNode

def main():
    test = textnode.TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) [rick roll](https://i.imgur.com/aKaOqIh.gif) and more text [another link](https://i.imgur.com/aKaOqIh.gif) and more text", textnode.TextType.NORMAL)
    print(textnode.split_nodes_link([test]))

if __name__ == "__main__":
    main()