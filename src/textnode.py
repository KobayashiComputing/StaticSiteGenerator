from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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
            case TextType.TEXT:
                return LeafNode(tag=None, value=self.text, props=None)
            case TextType.BOLD:
                return LeafNode(tag='b', value=self.text, props=None)
            case TextType.ITALIC:
                return LeafNode(tag='i', value=self.text, props=None)
            case TextType.CODE:
                return LeafNode(tag='code', value=self.text, props=None)
            case TextType.LINK:
                return LeafNode(tag='a', value=self.text, props={"href": self.url})
            case TextType.IMAGE:
                return LeafNode(tag='img', value='', props={"src": self.url, "alt": self.value})
            case _:
                raise Exception("unknown text type")


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        chunks = node.text.split(delimiter)
        if len(chunks) % 2 == 0:
            raise Exception(f"Unmatched delimiter {delimiter} in '{node.text}'")
        else:
            for ndx in range(len(chunks)):
                if chunks[ndx] == "":
                    continue
                if ndx % 2 == 0:
                    new_nodes.extend([TextNode(text=chunks[ndx], text_type=TextType.TEXT)])
                else:
                    new_nodes.extend([TextNode(text=chunks[ndx], text_type=text_type)])

    return new_nodes
