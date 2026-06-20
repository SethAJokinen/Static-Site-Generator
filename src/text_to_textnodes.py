from textnode import TextNode, TextType, split_nodes_delimiter
from image_and_link_splitter import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    new_text_node = TextNode(text, TextType.TEXT)
    nodes = [new_text_node]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes