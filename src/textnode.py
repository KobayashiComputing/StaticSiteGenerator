from enum import Enum
from htmlnode import *

class TextType(Enum):
    NORMAL_TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        if self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def to_html_node(self):
        match self.text_type:
            case TextType.NORMAL_TEXT:
                return LeafNode(tag=None, value=self.text, props=None)
            case TextType.BOLD_TEXT:
                return LeafNode(tag='b', value=self.text, props=None)
            case TextType.ITALIC_TEXT:
                return LeafNode(tag='i', value=self.text, props=None)
            case TextType.CODE_TEXT:
                return LeafNode(tag='code', value=self.text, props=None)
            case TextType.LINK_TEXT:
                return LeafNode(tag='a', value=self.text, props={"href": self.url})
            case TextType.IMAGE_TEXT:
                return LeafNode(tag='img', value='', props={"src": self.url, "alt": self.value})
            case _:
                raise Exception("unknown text type")


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK_TEXT:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE_TEXT:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")