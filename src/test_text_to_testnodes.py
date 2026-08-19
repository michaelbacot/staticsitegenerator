import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_text_to_textnodes_no_formatting(self):
        text = "This is a plain text with no formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is a plain text with no formatting.", TextType.TEXT),
        ])

    def test_text_to_textnodes_only_formatting(self):
        text = "**Bold** _Italic_ `Code` ![Image](https://example.com/image.png) [Link](https://example.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("Bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("Italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("Code", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("Image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("Link", TextType.LINK, "https://example.com"),
        ])