from textnode import TextNode, TextType
from extract_functions import extract_markdown_images, extract_markdown_links

def split_node_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        delimeter_count = node.text.count(delimeter)
        if delimeter_count % 2 != 0:
            raise Exception(f"Closing delimeter '{delimeter}' not found in node text: {node.text}")
        
        split_text = node.text.split(delimeter)
        for i, text in enumerate(split_text):
            if text == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            split_text = node.text.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node.text = split_text[1]

        if len(node.text) > 0:
            new_nodes.append(TextNode(node.text, TextType.TEXT))

    return new_nodes

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            split_text = node.text.split(f"[{link[0]}]({link[1]})", 1)
            new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node.text = split_text[1]

        if len(node.text) > 0:
            new_nodes.append(TextNode(node.text, TextType.TEXT))

    return new_nodes