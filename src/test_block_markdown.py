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

if __name__ == "__main__":
    unittest.main()