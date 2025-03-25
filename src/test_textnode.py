import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a textnode", TextType.BOLD)
        node2 = TextNode("This is a textnode", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif_text(self):
        node = TextNode("This is textnode 1", TextType.BOLD)
        node2 = TextNode("This is textnode 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_dif_type(self):
        node = TextNode("This is a textnode", TextType.BOLD)
        node2 = TextNode("This is a textnode", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_dif_url(self):
        node = TextNode("This is a textnode", TextType.BOLD)
        node2 = TextNode("This is a textnode", TextType.BOLD, "https://www.youtube.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()