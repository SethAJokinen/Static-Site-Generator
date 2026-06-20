import unittest
from image_and_link_splitter import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestSplitters(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_image_and_link(self):
            node = TextNode(
                "This is text with a [link](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da) and ![image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with a [link](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da) and ", TextType.TEXT),
                    TextNode(
                        "image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                    ),
                ],
                new_nodes,
            )
    
    def test_split_image_and_link_two(self):
            node = TextNode(
                "This is text with a [link](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da) and ![image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da"),
                    TextNode(" and ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)

                ],
                new_nodes,
            )
    
    def text_text_to_textnodes(self):
          node_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
          new_nodes = text_to_textnodes(node_text)

          correct = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ]
          self.assertListEqual(node_text, correct)