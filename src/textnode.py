import leafnode
import re
from enum import Enum

class TextType(Enum):
    
    NORMAL = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():

    def __init__(self, text: str, text_type: TextType = TextType.NORMAL, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text_type == other.text_type
    
    def __repr__(self):
        return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"
    
    def extract_markdown_images(self):

        if self.text_type == TextType.IMAGE:
            return [(self.text, self.url)]

        if self.text_type != TextType.NORMAL:
            raise TypeError(f"{self.text_type} is not of type {TextType.NORMAL}")
    
        REGEX_MARKDOWN_IMAGE = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        image_matches = re.findall(REGEX_MARKDOWN_IMAGE, self.text)

        return image_matches
    
    def extract_markdown_links(self):

        if self.text_type == TextType.LINK:
            return [(self.text, self.url)]
        
        if self.text_type != TextType.NORMAL:
            raise TypeError(f"{self.text_type} is not of type {TextType.NORMAL}")
        
        REGEX_MARKDOWN_LINK = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        link_matches = re.findall(REGEX_MARKDOWN_LINK, self.text)

        return link_matches
    
    def is_identical(self, other):
        return self == other and self.text == other.text and self.url == other.url
    
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

def extract_markdown_images(text):
    MARKDOWN_IMAGE_REGEX = r"!\[.*?\]\(.*?\)"
    image_matches = re.findall(MARKDOWN_IMAGE_REGEX, text)


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
            new_nodes.append(TextNode(node.text[:first_delim]))

        matched_delim = node.text.find(delimiter, first_delim + 1)
        if matched_delim == -1:
            raise TypeError(f"split_node_delimiter: could not find matching delimiter for \"{delimiter}\"")
        
        new_nodes.append(TextNode(node.text[first_delim+len(delimiter):matched_delim], text_type))
       
        remaining_text = node.text[matched_delim+len(delimiter):]
        if remaining_text:
            new_nodes.extend(
                split_nodes_delimiter(
                    [TextNode(remaining_text)],
                    delimiter=delimiter,
                    text_type=text_type
                )
            )
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    if not old_nodes:
        return []
    
    new_nodes = []
    for node in old_nodes:
        extracted_images = node.extract_markdown_images()
        if not extracted_images:
            new_nodes.append(node)
            continue

        next_image = f"![{extracted_images[0][0]}]({extracted_images[0][1]})"
        image_index = node.text.find(next_image)
        
        pre_image = node.text[:image_index]
        if pre_image:
            new_nodes.extend(
                split_nodes_image([TextNode(pre_image)])
            )

        new_nodes.append(
            [TextNode(extracted_images[0][0], TextType.IMAGE, extracted_images[0][1])]
        )

        post_image = node.text[image_index+len(next_image):]
        if post_image:
            new_nodes.extend(
                split_nodes_image([TextNode(post_image)])
            )

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
    if not old_nodes:
        return []
    
    new_nodes = []
    for node in old_nodes:
        extracted_links = node.extract_markdown_links()
        if not extracted_links:
            new_nodes.append(node)
            continue

        next_link = f"[{extracted_links[0][0]}]({extracted_links[0][1]})"
        link_index = node.text.find(next_link)
        
        pre_link = node.text[:link_index]
        if pre_link:
            new_nodes.extend(
                split_nodes_link([TextNode(pre_link)])
            )

        new_nodes.append(
            [TextNode(extracted_links[0][0], TextType.LINK, extracted_links[0][1])]
        )

        post_link = node.text[link_index+len(next_link):]
        if post_link:
            new_nodes.extend(
                split_nodes_link([TextNode(post_link)])
            )

    return new_nodes