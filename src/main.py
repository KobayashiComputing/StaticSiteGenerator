from textnode import *
from htmlnode import *


def main():
    t1 = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    t2 = TextNode("This is an image of Allen", TextType.IMAGE_TEXT, "allen.png")
    print(t1.__repr__())
    print(t2.__repr__())
    print(f"t1 and t2 are equal! ({t1.__eq__(t2)})")

    h1 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
    print(h1.__repr__())
    print(f"attributes are: {h1.props_to_html()}")

    l1 = LeafNode("p", "This is a paragraph of text")
    print(l1.to_html())
    l2 = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
    print(l2.to_html())

    child_list = [l1, l2]
    p1 = ParentNode("div", child_list, {"id": "front_page", "class": "main_window"})
    print(p1.to_html())

    



main()
