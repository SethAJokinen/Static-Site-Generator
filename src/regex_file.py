import re

def extract_markdown_images(text):
    matches_list = None 
    matches_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches_list


def extract_markdown_links(text):
    matches_list = None 
    matches_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches_list


