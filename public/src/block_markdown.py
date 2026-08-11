def markdown_to_blocks(markdown: str) -> list[str]:
    final_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if len(block) != 0:
            final_blocks.append(block)
    return final_blocks