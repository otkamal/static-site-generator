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
        return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"
    
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
        
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if not old_nodes:
        return []
    new_nodes = []
    
    for node in old_nodes:
        first_delim = node.text.find(delimiter)
        if node.text_type != TextType.NORMAL or first_delim == -1:
            new_nodes.append(node)
            continue

        if first_delim > 0:
            new_nodes.append(TextNode(node.text[:first_delim], TextType.NORMAL))

        matched_delim = node.text.find(delimiter, first_delim + 1)
        if second == -1:
            raise TypeError(f"split_node_delimiter: could not find matching delimiter for \"{delimiter}\"")
        
        new_nodes.append(TextNode(node.text[first_delim+len(delimiter):second], text_type))
       
        remaining_text = node.text[second+len(delimiter):]
        if remaining_text:
            new_nodes.extend(
                split_nodes_delimiter(
                    [TextNode(remaining_text, TextType.NORMAL)],
                    delimiter=delimiter,
                    text_type=text_type
                )
            )

    return new_nodes