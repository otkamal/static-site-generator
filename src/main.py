import textnode

def main():
    test = textnode.TextNode("test node", textnode.TextType.BOLD, "https://google.com")
    print(test)

if __name__ == "__main__":
    main()