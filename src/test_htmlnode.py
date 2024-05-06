import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", "bold")
        node2 = HTMLNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("This is a text node", "bold")
        node2 = HTMLNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_props_encode(self):
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(expected, node.props_to_html())


if __name__ == "__main__":
    unittest.main()
