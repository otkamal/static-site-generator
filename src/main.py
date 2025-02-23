import textnode
import htmlnode
import parentnode
import mdprocessing
from leafnode import LeafNode

def main():

    with open("public/test.md", "r") as md:
        mdprocessing.markdown_to_HTMLNode(md.read())
        
if __name__ == "__main__":
    main()