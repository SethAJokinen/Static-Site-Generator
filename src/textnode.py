from enum import Enum
from htmlnode import LeafNode


class TextType(str, Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, URL=None):
        self.text = text
        self.text_type = text_type
        self.url = URL

    def __eq__(self, other):
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url:
                    return True
        return False
    
    def __repr__(self):
       return f"TextNode({self.text},{self.text_type.value},{self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError("Not an acceptable text type!")
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        props = {
            "href": f"{text_node.url}"
        }
        return LeafNode(tag="a", value=text_node.text, props=props)
    if text_node.text_type == TextType.IMAGE:
        props = {
            "src": f"{text_node.url}",
            "alt": f"{text_node.text}"
        }
        return LeafNode(tag="img", value=text_node.text, props=props)
    return LeafNode(tag=None, value=text_node.text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError('No matching delimiter found!')
        text_list = node.text.split(delimiter)
        for i in range(len(text_list)):
            if i % 2 == 0:
                new_text_node = TextNode(text_list[i], text_type=TextType.TEXT)
                new_nodes.append(new_text_node)
            else:
                new_text_node = TextNode(text_list[i], text_type=text_type)
                new_nodes.append(new_text_node)
    return new_nodes
        