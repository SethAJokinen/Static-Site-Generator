from regex_file import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_image_text = extract_markdown_images(node.text)
        if not node_image_text:
            new_nodes.append(node)
            continue
        remaining_text = node.text

        for image_tuple in node_image_text:
            alt_text, img_url = image_tuple
            sections = remaining_text.split(f"![{alt_text}]({img_url})", 1)
            if sections[0]:
                new_text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(new_text_node)
            new_img_node = TextNode(alt_text, TextType.IMAGE, img_url)
            new_nodes.append(new_img_node)
            remaining_text = sections[1]
        
        if remaining_text:
                new_text_node = TextNode(remaining_text, TextType.TEXT)
                new_nodes.append(new_text_node)
    
    return new_nodes
    

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_link_text = extract_markdown_links(node.text)
        if not node_link_text:
            new_nodes.append(node)
            continue
        remaining_text = node.text

        for link_tuple in node_link_text:
            alt_text, link_url = link_tuple
            sections = remaining_text.split(f"[{alt_text}]({link_url})", 1)
            if sections[0]:
                new_text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(new_text_node)
            new_link_node = TextNode(alt_text, TextType.LINK, link_url)
            new_nodes.append(new_link_node)
            remaining_text = sections[1]
        
        if remaining_text:
                new_text_node = TextNode(remaining_text, TextType.TEXT)
                new_nodes.append(new_text_node)
    
    return new_nodes
            