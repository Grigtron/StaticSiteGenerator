import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("If I only had a brain", TextType.ITALIC)
        node4 = TextNode("What would you do for a Klondike bar?", TextType.ITALIC)
        node5 = TextNode("If I only had a brain", TextType.ITALIC)
        node6 = TextNode("This is a text node", TextType.ITALIC)
        node7 = TextNode("If I only had a brain", TextType.BOLD)
        node8 = TextNode("What would you do for a Klondike bar?", TextType.ITALIC)
        
        self.assertEqual(node, node2)
        self.assertEqual(node3, node5)
        self.assertEqual(node4, node8)
        ##self.assertEqual(node7, node3)
        ##self.assertEqual(node, node6)
        


if __name__ == "__main__":
    unittest.main()