from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    final_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if len(block) != 0:
            final_blocks.append(block)
    return final_blocks

def block_to_block_type(block: str) -> BlockType:
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith(("- ", "* ")):
        return BlockType.ULIST
    elif block[0].isdigit() and block[1:3] == ". ":
        return BlockType.OLIST
    elif block.startswith("```"):
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH
