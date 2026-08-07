import re

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    Extracts links from a markdown raw test string.
    Returns a list of tuples of ('alt text', 'url')
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_images(test: str) -> list[tuple[str, str]]:
    """
    Extracts images from a markdown raw test string.
    Returns a list of tuples of ('alt text', 'url')
    """
    pattern = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, test)
    return matches