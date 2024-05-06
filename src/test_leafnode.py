import unittest

from htmlnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == '__main__':
    unittest.main()
