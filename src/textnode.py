import leafnode

from enum import Enum

class TextType(Enum):
    
    NORMAL = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():

    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text_type == other.text_type
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def to_HTMLNode(self):
        if self.text_type == TextType.IMAGE:
            return leafnode.LeafNode(
                tag = self.text_type.value,
                value = "",
                props = {
                    "src" : self.url,
                    "alt" : self.text
                }
            )
        elif self.text_type == TextType.LINK:
            return leafnode.LeafNode(
                tag = self.text_type.value,
                value = self.text,
                props = {
                    "href" : self.url
                }
            )
        else:
            return leafnode.LeafNode(
                tag = self.text_type.value,
                value = self.text
            )