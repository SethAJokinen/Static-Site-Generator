from enum import Enum
from markdown_to_blocks import markdown_to_blocks
import re

class BlockType(str, Enum):
    HEADING = "heading",
    QUOTE = "quote",
    CODE = "code",
    UNORDERED_LIST = "unordered list",
    ORDERED_LIST = "ordered list",
    PARAGRAPH = "paragraph"


def block_to_block_type(markdown):
    pattern = r"^#{1,6} "
    if re.match(pattern, markdown):
        return BlockType.HEADING
    
    pattern = r"^`{3}(.*)\n"
    if re.match(pattern, markdown):
        if markdown.endswith("```"):
            return BlockType.CODE

    split_markdown = markdown.split("\n")

    pattern = r"^> {0,1}"
    if re.match(pattern, markdown):
        for md in split_markdown:
            if not re.match(pattern, md):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    
    pattern = r"^- "
    if re.match(pattern, split_markdown[0]):
        for md in split_markdown:
            if not re.match(pattern, md):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    counter = 1
    pattern = rf"^{counter}\. "
    if re.match(pattern, split_markdown[0]):
        for md in split_markdown:
            if not re.match(pattern, md):
                return BlockType.PARAGRAPH
            counter += 1
            pattern = rf"^{counter}\. "
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
