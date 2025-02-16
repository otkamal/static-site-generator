import htmlnode

class ParentNode(htmlnode.HTMLNode):

    def __init__(self, tag: str = None, children: list = None, props: dict = None):
        if tag is None or children is None or len(children) == 0:
            raise ValueError("ParentNode must have tag and children")
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("node does not have tag")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for c in self.children:
            try:
                html_string += c.to_html()
            except ValueError as e:
                print(e)
                exit(1)
        html_string += f"</{self.tag}>"
        return html_string        