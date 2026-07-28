from typing import Dict, List, Optional

class HTMLNode():
    def __init__(
        self, 
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in subclasses")

    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        for key, value in self.props.items():
            return f' {key}="{value}"'

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, props: {self.props})"
