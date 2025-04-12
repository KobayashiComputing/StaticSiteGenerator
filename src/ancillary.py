def markdown_to_blocks(markdown):
    block_list = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 0:
            block_list.append(block)
    return block_list