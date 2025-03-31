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

if __name__ == "__main__":
    unittest.main()