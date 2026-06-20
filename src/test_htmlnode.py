import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import text_node_to_html_node
from textnode import TextNode
from textnode import TextType

class TestHTMLNode(unittest.TestCase):
    def test_props_test_one(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(tag="<a>", value='something',children=None, props=props)
        result = node.props_to_html()
        correct_result =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, correct_result)

    def test_props_test_two(self):
        props = {}
        node = HTMLNode(tag="div",value="content", children=None,props=props)
        result = node.props_to_html()
        correct_result = ""
        self.assertEqual(result, correct_result)


    def test_leaf_test_one(self):
        leaf = LeafNode(tag="p",value="This is a paragraph.", props=None)
        result = leaf.to_html()
        correct_result = "<p>This is a paragraph.</p>"
        self.assertEqual(result, correct_result)

    def test_leaf_test_two(self):
        props = {
            "href": "https://www.google.com"
        }
        leaf = LeafNode(tag="a", value="This is an anchor tag.", props=props)
        result = leaf.to_html()
        correct = '<a href="https://www.google.com">This is an anchor tag.</a>'
        self.assertEqual(result, correct)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

 


if __name__ == "__main__":
    unittest.main()