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

    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(f"{parent_node.to_html()} should be: <div><span>child</span></div>")

    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(f"{parent_node.to_html()} should be: <div><span><b>grandchild</b></span></div>")
    
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(f"{node.to_html()}")

    node = TextNode("This is a text node", TextType.NORMAL_TEXT)
    html_node = node.to_html_node()
    print(f"{html_node.tag} should equal {None}")
    print(f"{html_node.value} should equal 'This is a text node'")

    node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

main()
