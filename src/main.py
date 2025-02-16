import textnode
import htmlnode

def main():
    test = textnode.TextNode("test node", textnode.TextType.BOLD, "https://google.com")
    test2 = htmlnode.HTMLNode("a", "hello", [htmlnode.HTMLNode(), htmlnode.HTMLNode()])
    print(test2)

if __name__ == "__main__":
    main()