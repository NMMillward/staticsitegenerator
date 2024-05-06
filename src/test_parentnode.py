import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, None, None)
            node.to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("test", None, None)
            node.to_html()

    def test_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        result = node.to_html()
        self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_with_parent_child(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text")
                    ],
                )
            ],
        )

        result = node.to_html()
        self.assertEqual(result, "<p><b>Bold text</b><p><b>Bold text</b></p></p>")


if __name__ == '__main__':
    unittest.main()
