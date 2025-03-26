import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="h1", value="something", children="children", props={"something1":"thing1", "something2": "thing2"})
        self.assertNotEqual(node, None)

    def test_props_empty(self):
        sample_node = HTMLNode(tag="h1", value="sample text", children="some children")
        self.assertEqual(sample_node.props_to_html(), "")

    def test_props_single(self):
        sample_node = HTMLNode(tag="h1", value="sample text", children="some children", props={"href": "https://www.google.com"})
        self.assertEqual(sample_node.props_to_html(), ' href="https://www.google.com"')

    def test_props_multiple(self):
        sample_node = HTMLNode(tag="h1", value="sample text", children="some children", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(sample_node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    ### Leaf Node

    def test_leaf_html_no_value(self):
        sample_leaf = LeafNode('h1', None, props={"href": "https://www.google.com", "target": "_blank",})
        with self.assertRaises(ValueError):
            sample_leaf.to_html()
    
    def test_leaf_html_no_tag(self):
        sample_leaf = LeafNode(None, 'Something', props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(sample_leaf.to_html(), "Something")

    def test_leaf_html_normal(self):
        sample_leaf = sample_leaf = LeafNode('p', 'Something', props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(sample_leaf.to_html(), '<p href="https://www.google.com" target="_blank">Something</p>')


    ### Parent Node
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__=="__main__":
    unittest.main()