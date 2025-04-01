import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<div>", value=None, children=None, props={"id": "page_header", "class": "header"})
        node2 = HTMLNode("<div>", value=None, children=None, props={"id": "page_header", "class": "header"})
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_not_eq(self):
        node = HTMLNode("<div>", value=None, children=None, props={"id": "page_header", "class": "header"})
        node2 = HTMLNode("<div>", value=None, children=None, props={"id": "page_footer", "class": "footer"})
        self.assertNotEqual(node.__repr__(), node2.__repr__())

    def test_by_string_eq(self):
        HTMLString = "HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        node = HTMLNode(None, None, None,  {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), HTMLString)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        l = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(l.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_leaf_no_tag(self):
        l = LeafNode(None, "This is just plain text.")
        self.assertEqual(l.to_html(), "This is just plain text.")

if __name__ == "__main__":
    unittest.main()