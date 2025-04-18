from enum import Enum
from htmlnode import *
from textnode import *
from extractors import *

def markdown_to_blocks(markdown):
    block_list = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 0:
            block_list.append(block)
    return block_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "ulist"
    OLIST = "olist"


def block_to_block_type(block):
    block_type = BlockType.PARAGRAPH

    # It's a heading if it begins with from 1 to 6 '#' characters...
    if block[0] == "#":
        ndx = block.index(" ")
        if ndx > 0 and ndx < 7 and "###### "[:ndx] == block[:ndx]:
            block_type = BlockType.HEADING
    
    # It's a code block if it both starts and ends with "```"
    elif block[:3] == "```" and block[-3:] == "```":
        block_type = BlockType.CODE
    
    # It's a quote block if every line starts with a '>'
    elif block[0] == '>':
        block_type = BlockType.QUOTE
        lines = block.splitlines()
        for line in lines:
            if line[0] != '>':
                block_type = BlockType.PARAGRAPH

    # It's an unordered list if every line starts with "- "
    elif block[:2] == "- ":
        block_type = BlockType.ULIST
        lines = block.splitlines()
        for line in lines:
            if line[:2] != "- ":
                block_type = BlockType.PARAGRAPH
    
    # It's an ordered list if the first line starts with "1. " and then increments
    elif block[:3] == "1. ":
        block_type = BlockType.OLIST
        lines = block.splitlines()
        counter = 0
        for line in lines:
            counter += 1
            digit_count = len(f"{counter}".strip()) + 2
            if line[:digit_count] != f"{counter}. ":
                block_type = BlockType.PARAGRAPH

    # Anything else should be a plain paragraph...
    else:
        block_type = BlockType.PARAGRAPH

    return block_type

def markdown_to_html_node(markdown):
    # each complete markdown string (or 'file') becomes a <div> in html (?!),
    # and the blocks in the markdown become the children of the <div>
    div_children = []
    # break the markdown file into blocks, defined by two newlines in a row
    block_list = markdown_to_blocks(markdown)
    # each block of markdown becomes one of the six canonical types of html blocks
    for block in block_list:
        # get the current block type, which will dictate how we handle this block
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                # paragraph block parts get broken down into leaf nodes... (text nodes...)
                # in HTML paragraph text, newlines are ignored, so convert them to spaces
                block = block.replace('\n', ' ')
                # next, break the block of text into text nodes
                node_list = text_to_text_nodes(block)
                html = ""
                for node in node_list:
                    leaf_node = node.to_html_node()
                    html += leaf_node.to_html()
                div_children.append(LeafNode(tag="p", value=html, props=None))
                pass
            case BlockType.HEADING:
                # heading blocks *should* be only a single line, but, I presume, could
                # contain **bold** or _italic_ or `code` parts, and get broken down into 
                # leaf nodes... (text nodes...)
                # do we need to remove newlines in the block?
                block = block.replace('\n', ' ')
                # we need to count the number of leading '#' to get the "h" level (h1 - h6)
                # for the tag...
                count = block.index(" ")
                # count = 1 # for now...
                block = (block.replace('#', '', count)).strip()
                # next, break the block of text into text nodes
                node_list = text_to_text_nodes(block)
                html = ""
                for node in node_list:
                    leaf_node = node.to_html_node()
                    html += leaf_node.to_html()
                div_children.append(LeafNode(tag=f"h{count}", value=html, props=None))
                pass
            case BlockType.CODE:
                # code blocks get mostly left alone - just stripped of their delimieters
                # but with no further changes
                block = (block[3:])[:-3]
                node = LeafNode(tag="code", value=block, props=None)
                html = node.to_html()
                div_children.append(LeafNode(tag="pre", value=html, props=None))
                pass
            case BlockType.QUOTE:
                # first, get rid of the ">" chars at the beginning of each line
                lines = block.splitlines()
                new_lines = []
                for line in lines:
                    new_lines.append(line[2:].strip())
                block = ' '.join(new_lines)
                # block quotes are like paragraphs in that linebreaks are ignored
                block = block.replace('\n', ' ').strip()
                # block parts get broken down into leaf nodes... (text nodes...)
                # next, break the block of text into text nodes
                node_list = text_to_text_nodes(block)
                html = ""
                for node in node_list:
                    leaf_node = node.to_html_node()
                    html += leaf_node.to_html()
                div_children.append(LeafNode(tag="blockquote", value=html, props=None))
                pass
            case BlockType.OLIST:
                pass
            case BlockType.ULIST:
                pass
        
    html_tree = ParentNode(tag="div", children=div_children, props=None)


    pass

    return html_tree
