import unittest
from htmlnode import *
from textnode import *


class TestTextNodeToHTMLNode:
    def test_text_type(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == ""
        assert html_node.value == "Hello, world!"
        assert html_node.props == None

    def test_bold_type(self):
        text_node = TextNode("If I only had a brain", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == "If I only had a brain"
        assert html_node.props == None
    
    def test_italic_type(self):
        text_node = TextNode("Somebody once told me", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "i"
        assert html_node.value == "Somebody once told me"
        assert html_node.props == None

    def test_code_type(self):
        text_node = TextNode("The world is gonna roll me", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "code"
        assert html_node.value == "The world is gonna roll me"
        assert html_node.props == None

    def test_links_type(self):
        text_node = TextNode("https://www.boot.dev", TextType.LINKS)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "https://www.boot.dev"
        assert html_node.props == {"href": "https://www.boot.dev"}

    def test_images_type(self):
        text_node = TextNode("The Shape of an L on a forehead", TextType.IMAGES, "https://imgur.com/JyyefuX")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "https://imgur.com/JyyefuX", "alt": "The Shape of an L on a forehead"}

    def test_invalid_text_type(self):
        text_node = TextNode("Well, the years start coming", None)
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(text_node)
            assert html_node == "Not a valid TextType"

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode:(p, What a strange world, None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_render_as_raw_text(self):
        node = LeafNode(tag=None, value="What a strange world", props=None)
        self.assertEqual(node.to_html(), "What a strange world")
        

    def test_value_error_on_none_value(self):
        node = LeafNode("p", value=None, props=None)
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_render_as_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),
                         '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_parent_node_creation(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], {})
        self.assertIsInstance(node, ParentNode)

    def test_tag_cannot_be_none(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Content")])

    def test_children_cannot_be_none(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)
    
    def test_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])
    
    def test_render_with_leaf_nodes(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello"),
            LeafNode("a", "Link", {"href": "https://www.boot.dev"})
        ])
        expected_html = '<div><p>Hello</p><a href="https://www.boot.dev">Link</a></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_nested_parent_nodes(self):
        child_node = ParentNode("section", [
            LeafNode("p", "Nested content")
        ])
        parent_node = ParentNode("div", [child_node])
        expected_html = '<div><section><p>Nested content</p></section></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

                                    

if __name__ == "__main__":
    unittest.main()