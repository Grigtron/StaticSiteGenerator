from textnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode("", text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})      
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Not a valid TextType")
        
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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        

    def to_html(self):
        if self.value is None:
            raise ValueError("value cannot be None")
        if self.tag is None:
            return f"{self.value}"
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if self.children is None:
            raise ValueError("children cannot be None")
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if len(self.children) == 0:
            raise ValueError("children cannot be an empty list")
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if self.children is None:
            raise ValueError("children cannot be None")
        
        if not self.children:
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"
        html_content = ""
        for child_node in self.children:
            html_content += child_node.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_content}</{self.tag}>"