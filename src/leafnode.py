import htmlnode
import warnings

class LeafNode(htmlnode.HTMLNode):

    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        if value is None:
            raise TypeError("leafnode value must be set")
        super().__init__(tag = tag, value = value, children = None, props = props)
        
    def to_html(self):
        if self.value is None:
            raise TypeError("leafnode value must be set")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" 
        
