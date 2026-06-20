import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlock(unittest.TestCase):
    def test_block_heading_one(self):
        self.assertEqual(block_to_block_type("### This is a heading,"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### This is also a heading,"), BlockType.HEADING)

    def test_block_heading_two(self):
        self.assertEqual(block_to_block_type("####### Too many #'s"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    def test_block_ordered_list(self):
        test_ordered = """1. This
2. is
3. List"""
        test_not_ordered = """1. This
2. is
3. Not
5. List"""
        self.assertEqual(block_to_block_type(test_ordered), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(test_not_ordered), BlockType.PARAGRAPH)
    
    def test_quotes(self):
        quote = """>This
>is
>a
> quote"""
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

        not_quote = """>This
        not
        >a
        >quote"""
        self.assertEqual(block_to_block_type(not_quote), BlockType.PARAGRAPH)