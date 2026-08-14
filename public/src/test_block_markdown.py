import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item"), BlockType.ULIST)
        self.assertEqual(block_to_block_type("1. Ordered list item"), BlockType.OLIST)
        self.assertEqual(block_to_block_type("```code block```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_markdown_to_blocks_type(self):
        md = """
This is **bolded** paragraph

```
This is a code block
```


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.PARAGRAPH,
                BlockType.CODE,
                BlockType.PARAGRAPH,
                BlockType.ULIST,
            ],
        )