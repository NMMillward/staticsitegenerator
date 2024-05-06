class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop_key in self.props.keys():
            props_html += f" {prop_key}=\"{self.props[prop_key]}\""
        return props_html

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        prop_html = self.props_to_html()
        if self.tag is None:
            return self.value
        return f"<{self.tag}{prop_html}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None:
            raise ValueError("No children provided")

        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
