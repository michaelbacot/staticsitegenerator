from textnode import TextNode, TextType

def split_node_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)

        delimeter_count = node.text.count(delimeter)
        if delimeter_count % 2 != 0:
            raise Exception(f"Closing delimeter '{delimeter}' not found in node text: {node.text}")
        
        split_text = node.text.split(delimeter)
        for i, text in enumerate(split_text):
            if i % 2 == 0 and len(text) > 0:
                new_nodes.append(TextNode(text, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(text, text_type))
                
    return new_nodes