import unittest

from textnode import *


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_delimiter_for_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        check_nodes = [TextNode("This is text with a ", TextType.NORMAL_TEXT), TextNode("code block", TextType.CODE_TEXT), TextNode(" word", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_code_2(self):
        node = TextNode("This is text with a `code block` here and a `code block` there.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        check_nodes = [TextNode("This is text with a ", TextType.NORMAL_TEXT), TextNode("code block", TextType.CODE_TEXT), TextNode(" here and a ", TextType.NORMAL_TEXT), TextNode("code block", TextType.CODE_TEXT), TextNode(" there.", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)
    
    def test_delimiter_for_code_3(self):
        node = TextNode("This is text with no code blocks at all!", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        check_nodes = [TextNode("This is text with no code blocks at all!", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        check_nodes = [TextNode("This is text with a ", TextType.NORMAL_TEXT), TextNode("bold", TextType.BOLD_TEXT), TextNode(" word", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_bold_2(self):
        node = TextNode("This is text with a **bold** word here and a **bold** word there.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        check_nodes = [TextNode("This is text with a ", TextType.NORMAL_TEXT), TextNode("bold", TextType.BOLD_TEXT), TextNode(" word here and a ", TextType.NORMAL_TEXT), TextNode("bold", TextType.BOLD_TEXT), TextNode(" word there.", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)
    
    def test_delimiter_for_bold_3(self):
        node = TextNode("This is text with no bold words at all!", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        check_nodes = [TextNode("This is text with no bold words at all!", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        check_nodes = [TextNode("This is text with an ", TextType.NORMAL_TEXT), TextNode("italic", TextType.ITALIC_TEXT), TextNode(" word", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)

    def test_delimiter_for_italic_2(self):
        node = TextNode("This is text with an _italic_ word here and an _italic_ word there.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        check_nodes = [TextNode("This is text with an ", TextType.NORMAL_TEXT), TextNode("italic", TextType.ITALIC_TEXT), TextNode(" word here and an ", TextType.NORMAL_TEXT), TextNode("italic", TextType.ITALIC_TEXT), TextNode(" word there.", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)
    
    def test_delimiter_for_italic_3(self):
        node = TextNode("This is text with no italic words at all!", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        check_nodes = [TextNode("This is text with no italic words at all!", TextType.NORMAL_TEXT)]
        self.assertEqual(new_nodes, check_nodes)





class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE_TEXT, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()