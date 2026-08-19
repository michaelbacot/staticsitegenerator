from textnode import TextNode, TextType
from inline_markdown import split_node_delimeter, split_nodes_images, split_nodes_links

def text_to_textnodes(text: str) -> list[TextNode]:
    """
    Converts a raw text string into a list of TextNode objects.
    """
    new_nodes = []
    initial_node = TextNode(text, TextType.TEXT)
    new_nodes = split_node_delimeter([initial_node], "**", TextType.BOLD)
    new_nodes = split_node_delimeter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_node_delimeter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_images(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    return new_nodes