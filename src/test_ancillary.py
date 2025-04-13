import unittest

from ancillary import *

class TestAncillaryFunctions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_type_code(self):
        block = "```\nfirst line of code\nsecond line of code\nthird line of code\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_block_type_heading_1(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_heading_2(self):
        block = "## Heading 2"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_heading_3(self):
        block = "### Heading 3"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_heading_4(self):
        block = "#### Heading 4"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_heading_5(self):
        block = "##### Heading 5"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_heading_6(self):
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_type_heading_7_not(self):
        block = "####### Heading 7 (Ha! That doesn't exist!)"
        self.assertNotEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_quote_with_space(self):
        block = "> first line of quote\n> second line of quote\n> third line of quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_block_type_quote_without_space(self):
        block = ">first line of quote\n>second line of quote\n>third line of quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_block_type_ulist(self):
        block = "- first line of unordered list\n- second line of unordered list\n- third line of unordered list"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
    
    def test_block_type_olist(self):
        block = """1. first line of ordered list
2. second line of ordered list
3. third line of ordered list
4. third line of ordered list
5. third line of ordered list
6. third line of ordered list
7. third line of ordered list
8. third line of ordered list
9. third line of ordered list
10. third line of ordered list
11. third line of ordered list
12. third line of ordered list
13. third line of ordered list
"""
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)





if __name__ == "__main__":
    unittest.main()