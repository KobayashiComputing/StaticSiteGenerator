import unittest

from markdown import *

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


    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.__repr__()
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_headings(self):
        md = "# Main Page Heading"
        node = markdown_to_html_node(md)
        html = node.__repr__()
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Main Page Heading</h1></div>")

    def test_headings4(self):
        md = "#### H4 Level Heading"
        node = markdown_to_html_node(md)
        html = node.__repr__()
        html = node.to_html()
        self.assertEqual(html, "<div><h4>H4 Level Heading</h4></div>")


    def test_codeblock(self):
        md = """```This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = ""
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """> This is a block quote. It has some _italic_ text
> and some **bold** text that, I think, should be handled. I'm not
> sure if links and images should be handled. I'll write another
> test case with a link and/or an image.

"""

        node = markdown_to_html_node(md)
        html = ""
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a block quote. It has some <i>italic</i> text and some <b>bold</b> text that, I think, should be handled. I'm not sure if links and images should be handled. I'll write another test case with a link and/or an image.</blockquote></div>",
        )

    def test_ulist_block(self):
        md = """- This is an unordered list item...
- This is an unordered list item...
- This is an unordered list item...
"""

        node = markdown_to_html_node(md)
        html = ""
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list item...</li><li>This is an unordered list item...</li><li>This is an unordered list item...</li></ul></div>",
        )

    def test_olist_block(self):
        md = """1. line of ordered list
2. line of ordered list
3. line of ordered list
4. line of ordered list
5. line of ordered list
6. line of ordered list
7. line of ordered list
8. line of ordered list
9. line of ordered list
10. line of ordered list
11. line of ordered list
12. line of ordered list
"""

        node = markdown_to_html_node(md)
        html = ""
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li><li>line of ordered list</li></ol></div>",
        )

    def test_paragraphs2(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings_2(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote2(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )






if __name__ == "__main__":
    unittest.main()