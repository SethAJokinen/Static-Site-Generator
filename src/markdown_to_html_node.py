from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode
from htmlnode import ParentNode, LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(text):
    list_of_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        list_of_nodes.append(text_node_to_html_node(node))
    return list_of_nodes

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    all_block_nodes = []
    for block in block_list:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            count = 0
            for char in block:
                if char == "#":
                    count += 1
                else:
                    break
            tag = f"h{count}"
            heading_text = block[count + 1:]
            list_of_children = text_to_children(heading_text)
            heading_node = ParentNode(tag, list_of_children)
            all_block_nodes.append(heading_node)
        elif block_type == BlockType.CODE:
            tag = "code"
            code_text = block[4:-3]
            code_node = LeafNode(tag, code_text)
            pre_node = ParentNode("pre", [code_node])
            all_block_nodes.append(pre_node)
        elif block_type == BlockType.QUOTE:
            tag = "blockquote"
            new_lines = []
            quote_text = block.split("\n")
            for quote in quote_text:
                alt_quote = quote[1:].strip()
                new_lines.append(alt_quote)
            new_quote_lines = " ".join(new_lines)
            quote_children = text_to_children(new_quote_lines)
            quote_node = ParentNode(tag, quote_children)
            all_block_nodes.append(quote_node)
        elif block_type == BlockType.UNORDERED_LIST:
            tag = "ul"
            child_tag = "li"
            new_lines = []
            unordered_list_text = block.split("\n")
            for listing in unordered_list_text:
                alt_listing = listing[1:].strip()
                new_lines.append(ParentNode(child_tag, text_to_children(alt_listing)))
            unordered_list_node = ParentNode(tag, new_lines)
            all_block_nodes.append(unordered_list_node)
        elif block_type == BlockType.ORDERED_LIST:
            tag = "ol"
            child_tag = "li"
            new_nodes = []
            ordered_list_text = block.split("\n")
            for listing in ordered_list_text:
                alt_listing = listing.split(".", 1)[1].strip()
                alt_listing_inline = text_to_children(alt_listing)
                new_nodes.append(ParentNode(child_tag, alt_listing_inline))
            ordered_list_node = ParentNode(tag, new_nodes)
            all_block_nodes.append(ordered_list_node)
        else:
            new_paragraph_block = block.replace("\n", " ")
            paragraph_with_inline = text_to_children(new_paragraph_block)
            paragraph_node = ParentNode("p", paragraph_with_inline)
            all_block_nodes.append(paragraph_node)

    return ParentNode("div", all_block_nodes)



            




    return ParentNode("div", all_block_nodes)
            
            