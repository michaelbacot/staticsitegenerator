import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "my-class"})

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        self.assertEqual(node.props_to_html(), ' class="my-class"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", value="Hello", children=[])
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, children: [], props: {'class': 'my-class'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("p", "Click Me!", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<p href="https://example.com">Click Me!</p>')