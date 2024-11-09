import unittest

from textnode import *
from htmlnode import *
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        node = """# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        result = markdown_to_blocks(node)
        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(result, expected_result)

    def test_block_to_block_type_heading(self):
        text = "#### This is a heading"
        result = block_to_block_type(text)
        expected_result = 'heading'
        self.assertEqual(expected_result, result)

    def test_block_to_block_type_code(self):
        text = "```This is a code block```"
        result = block_to_block_type(text)
        expected_result = 'code'
        self.assertEqual(expected_result, result)

    def test_block_to_block_type_quote(self):
        text = '>This is\n>a quote\n>test'
        result = block_to_block_type(text)
        expected_result = 'quote'
        self.assertEqual(expected_result, result)
    
    def test_block_to_block_type_unordered_list(self):
        text = '* This is a\n- unordered list test'
        result = block_to_block_type(text)
        expected_result = 'unordered_list'
        self.assertEqual(expected_result, result)

    def test_block_to_block_type_ordered_list(self):
        text = '1. This is a\n2. ordered list\n3. test'
        result = block_to_block_type(text)
        expected_result = 'ordered_list'
        self.assertEqual(expected_result, result)
    
    def test_block_to_block_type_paragraph(self):
        text = 'This is a paragraph test'
        result = block_to_block_type(text)
        expected_result = 'paragraph'
        self.assertEqual(expected_result, result)

def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()