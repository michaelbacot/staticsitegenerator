from splitnodes import split_node_delimeter, split_nodes_images, split_nodes_links
from textnode import TextNode, TextType

import unittest

class TestSplitNodeDelimeter(unittest.TestCase):
    def test_split_node_delimeter(self):
        # Test case 1: Basic splitting with even number of delimiters
        nodes = [TextNode("This is *bold* text", TextType.PLAIN)]
        result = split_node_delimeter(nodes, "*", TextType.BOLD)
        assert len(result) == 3
        assert result[0].text == "This is "
        assert result[1].text == "bold"
        assert result[1].text_type == TextType.BOLD
        assert result[2].text == " text"

        # Test case 2: No delimiters present
        nodes = [TextNode("No delimiters here", TextType.PLAIN)]
        result = split_node_delimeter(nodes, "*", TextType.BOLD)
        assert len(result) == 1
        assert result[0].text == "No delimiters here"
        assert result[0].text_type == TextType.PLAIN

        # Test case 3: Odd number of delimiters (should raise an exception)
        nodes = [TextNode("This is *bold text", TextType.PLAIN)]
        try:
            split_node_delimeter(nodes, "*", TextType.BOLD)
            assert False, "Expected an exception for odd number of delimiters"
        except Exception as e:
            assert str(e) == "Closing delimeter '*' not found in node text: This is *bold text"

class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes
        )

    def test_split_images_no_images(self):
        node = TextNode(
            "This is text with no images",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.PLAIN),
            ],
            new_nodes
        )

    def test_split_images_multiple_images(self):
        node = TextNode(
            "![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/3elNhQu.png) and ![image3](https://i.imgur.com/4elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("", TextType.PLAIN),
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("image3", TextType.IMAGE, "https://i.imgur.com/4elNhQu.png"),
            ],
            new_nodes
        )

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes
        )

    def test_split_links_no_links(self):
        node = TextNode(
            "This is text with no links",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with no links", TextType.PLAIN),
            ],
            new_nodes
        )