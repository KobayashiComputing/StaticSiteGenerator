import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is an image node", TextType.LINK_TEXT, "https://srccraft.net")
        node2 = TextNode("This is an image node", TextType.LINK_TEXT, "https://srccraft.net")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("This is an image node", TextType.IMAGE_TEXT, "./image.png")
        node2 = TextNode("This is a text node", TextType.LINK_TEXT, "https://srccraft.net")
        self.assertNotEqual(node, node2)






if __name__ == "__main__":
    unittest.main()