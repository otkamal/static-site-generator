import json

class HTMLNode():

    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        if isinstance(props, dict) or props is None:
            self.props = props
        else:
            raise TypeError(f"invalid props for HTMLNode type: {type(props)}")

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_as_html = ""
        if self.props != None:
            for p in self.props.keys():
                props_as_html += f" {p}=\"{self.props[p]}\""
        return props_as_html
    
    def __repr__(self):

        def __to_json__():
            return json.dumps(
                self,
                default = lambda o : o.__dict__,
                sort_keys = False,
                indent = 4
            )
        
        return __to_json__()
    
