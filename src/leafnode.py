import htmlnode

class LeafNode(htmlnode.HTMLNode):

      def __init__(self, tag: str = None, value: str = None, props: dict = None):
        if isinstance(tag, str) or tag is None:
            self.tag = tag