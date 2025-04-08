import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is an image node", TextType.LINK, "https://srccraft.net")
        node2 = TextNode("This is an image node", TextType.LINK, "https://srccraft.net")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("This is an image node", TextType.IMAGE, "./image.png")
        node2 = TextNode("This is a text node", TextType.LINK, "https://srccraft.net")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_delimiter_for_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        check_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_code_2(self):
        node = TextNode("This is text with a `code block` here and a `code block` there.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        check_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" here and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" there.", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)
    
    def test_delimiter_for_code_3(self):
        node = TextNode("This is text with no code blocks at all!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        check_nodes = [TextNode("This is text with no code blocks at all!", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        check_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_bold_2(self):
        node = TextNode("This is text with a **bold** word here and a **bold** word there.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        check_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word here and a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word there.", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)
    
    def test_delimiter_for_bold_3(self):
        node = TextNode("This is text with no bold words at all!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        check_nodes = [TextNode("This is text with no bold words at all!", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        check_nodes = [TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_italic_2(self):
        node = TextNode("This is text with an _italic_ word here and an _italic_ word there.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        check_nodes = [TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word here and an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word there.", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)
    
    def test_delimiter_for_italic_3(self):
        node = TextNode("This is text with no italic words at all!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        check_nodes = [TextNode("This is text with no italic words at all!", TextType.TEXT)]
        self.assertEqual(new_nodes, check_nodes)





class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()