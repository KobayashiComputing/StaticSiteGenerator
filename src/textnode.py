from enum import Enum
from htmlnode import *
from extractors import *

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

def split_nodes_image(old_nodes):
    new_nodes = []
    inodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        for image in images:
            inodes.append(TextNode(text=image[0], text_type=TextType.IMAGE, url=image[1]))
            pass
        new_text = node.text
        for inode in inodes:
            sections = new_text.split(f"![{inode.text}]({inode.url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown: image tag not complete")
            if sections[0] != "":
                new_nodes.append(TextNode(text=sections[0], text_type=TextType.TEXT))
            new_nodes.append(inode)
            new_text = sections[1]
        if new_text != "":
            new_nodes.append(TextNode(text=new_text, text_type=TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    lnodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        for link in links:
            lnodes.append(TextNode(text=link[0], text_type=TextType.LINK, url=link[1]))
            pass
        new_text = node.text
        for lnode in lnodes:
            sections = new_text.split(f"[{lnode.text}]({lnode.url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown: link tag not complete")
            if sections[0] != "":
                new_nodes.append(TextNode(text=sections[0], text_type=TextType.TEXT))
            new_nodes.append(lnode)
            new_text = sections[1]
        if new_text != "":
            new_nodes.append(TextNode(text=new_text, text_type=TextType.TEXT))
    return new_nodes

def text_to_text_nodes(text):
    nodes = [TextNode(text=text, text_type=TextType.TEXT, url=None)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes