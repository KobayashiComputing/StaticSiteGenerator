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

main()
