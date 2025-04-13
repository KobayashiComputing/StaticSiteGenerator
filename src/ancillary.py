from enum import Enum


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
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


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

    # Anything else should be a plain paragraph...
    else:
        block_type = BlockType.PARAGRAPH

    return block_type

