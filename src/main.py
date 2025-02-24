import mdprocessing
from copystatic import copy_static

def main():

    # with open("public/test.md", "r") as md:
    #     print(mdprocessing.markdown_to_HTMLNode(md.read()))
    copy_static("static", "public")
        
if __name__ == "__main__":
    main()