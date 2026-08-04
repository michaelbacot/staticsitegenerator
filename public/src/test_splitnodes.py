from splitnodes import split_node_delimeter
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