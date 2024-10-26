class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        attributes = [f'{key}="{value}"' for key, value in self.props.items()]
        return " " + " ".join(attributes)
    
    def __repr__(self) -> str:
        return f'HTMLNode:({self.tag}, {self.value}, {self.children}, {self.props})'
