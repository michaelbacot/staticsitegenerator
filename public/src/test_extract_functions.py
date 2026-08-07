import re
from extract_functions import extract_markdown_links, extract_markdown_images
import unittest

class TestExtractFunctions(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is a [link](http://example.com) in markdown."
        expected = [("link", "http://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_images(self):
        text = (
            "This is an ![image](http://example.com/image.png) in markdown."
            " This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        expected = [
            ("image", "http://example.com/image.png"),
            ("image", "https://i.imgur.com/zjjcJKZ.png")
        ]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)