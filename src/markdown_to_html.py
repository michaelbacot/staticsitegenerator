from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html


def markdown_to_html_node(markdown: str) -> HTMLNode:
    block_html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            text_nodes = text_to_textnodes(block)
            html_children = [text_node_to_html(node) for node in text_nodes]
            html_node = ParentNode("p", html_children)

        if block_type == BlockType.HEADING:
            heading_count = block.count("#")
            text = block[heading_count + 1:].strip()
            text_nodes = text_to_textnodes(text)
            html_children = [text_node_to_html(node) for node in text_nodes]
            html_node = ParentNode(f"h{heading_count}", html_children)

        if block_type == BlockType.CODE:
            block = block.strip("```")
            block = block.lstrip("\n")
            html_node = ParentNode("pre", [LeafNode("code", block)])

        if block_type == BlockType.QUOTE:
            quote_content_lines = []
            quote_lines = block.split("\n")
            for line in quote_lines:
                if not line.startswith("> "):
                    raise Exception("invalid quote block")
                quote_line_text = line[2:]
                quote_content_lines.append(quote_line_text)
            quote_content = " ".join(quote_content_lines)
            text_nodes = text_to_textnodes(quote_content)
            quote_leaf_nodes = [text_node_to_html(node) for node in text_nodes]
            html_node = ParentNode("blockquote", quote_leaf_nodes)

        if block_type == BlockType.ULIST:
            list_line_parent_nodes = []
            list_lines = block.split("\n")
            for line in list_lines:
                text = line[2:]
                line_text_nodes = text_to_textnodes(text)
                line_leaf_nodes = [text_node_to_html(node) for node in line_text_nodes]
                list_line_parent_nodes.append(ParentNode("li", line_leaf_nodes))
            html_node = ParentNode("ul", list_line_parent_nodes)

        if block_type == BlockType.OLIST:
            list_line_parent_nodes = []
            list_lines = block.split("\n")
            for line in list_lines:
                text = line[3:]
                line_text_nodes = text_to_textnodes(text)
                line_leaf_nodes = [text_node_to_html(node) for node in line_text_nodes]
                list_line_parent_nodes.append(ParentNode("li", line_leaf_nodes))
            html_node = ParentNode("ol", list_line_parent_nodes)

        block_html_nodes.append(html_node)

    return ParentNode("div", block_html_nodes)
