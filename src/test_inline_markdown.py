import unittest
import re
from inline_markdown import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_none_markdown_images(self):
        node = "This is just plain text with [some links](https://example.com) but no images"
        result = extract_markdown_images(node)
        self.assertEqual(result, [])

    def test_none_markdown_links(self):
        node = "This is just some plain text with ![some images](someimages.jpg) but no links"
        result = extract_markdown_links(node)
        self.assertEqual(result, [])

    def test_multiple_markdown_images(self):
        node = "This is just some plain text with ![multiple images](image1.jpg) with some pretty ![useful information](image2.jpg)"
        result = extract_markdown_images(node)
        self.assertEqual(result, [("multiple images", "image1.jpg"), ("useful information", "image2.jpg")])

    def test_multiple_markdown_links(self):
        node = "This is just some plain text with [multiple links](https://www.boot.dev) to some pretty [useful things](https://www.google.com)"
        result = extract_markdown_links(node)
        self.assertEqual(result, [("multiple links", "https://www.boot.dev"), ("useful things", "https://www.google.com")])

    def test_markdown_images_special_urls(self):
        node = "Here's an image with spaces ![test](my image.jpg) and one with special chars ![test2](my@#$image.jpg)"
        result = extract_markdown_images(node)
        self.assertEqual(result, [("test", "my image.jpg"), ("test2", "my@#$image.jpg")])
  
    def test_markdown_images_special_alt(self):
        node = "Here's an image with ![test!@#$](image.jpg) and another with ![&*()^%](pic.png)"
        result = extract_markdown_images(node)
        self.assertEqual(result, [("test!@#$", "image.jpg"), ("&*()^%", "pic.png")])

    def test_markdown_images_empty_alt(self):
        node = "Here's an image with no alt text ![](image.jpg) and a normal one ![test](pic.png)"
        result = extract_markdown_images(node)
        self.assertEqual(result, [("", "image.jpg"), ("test", "pic.png")])

    def test_markdown_images_empty_urls(self):
        node = "Here's an image with empty URL ![test]() and another ![also empty]()"
        result = extract_markdown_images(node)
        self.assertEqual(result, [("test", ""), ("also empty", "")])


if __name__ == "__main__":
    unittest.main()