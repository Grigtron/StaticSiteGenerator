from enum import Enum
from textnode import *
from htmlnode import *
from inline_markdown import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_block = "\n".join(line.strip() for line in block.splitlines())
        if stripped_block:
            filtered_blocks.append(stripped_block)
    return filtered_blocks

def block_to_block_type(text):
    if text.startswith("#"):
        hash_count = 0
        for char in text:
            if char == '#':
                hash_count += 1
            else:
                break
        if 1 <= hash_count <= 6 and text[hash_count] == ' ':
            return block_type_heading
    elif text.startswith('```') and text.endswith('```'):
        return block_type_code
    elif all(line.startswith('>') for line in text.split('\n')):
        return block_type_quote
    elif all((line.startswith('*') and line[1] == ' ') or (line.startswith('-') and line[1] == ' ') for line in text.split('\n')):
        return block_type_ulist
    elif all(line[0].isdigit() and int(line[0]) == (i + 1) and line[1] == '.' and line[2] == ' ' for i, line in enumerate(text.split('\n'))):
        return block_type_olist
    else:
        return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children 

def heading_to_html_node(block):
    hash_count = 0
    for char in block:
        if char == '#':
            hash_count += 1
        else:
            break
    if hash_count >= len(block):
        raise ValueError(f"Invalid heading level: {hash_count}")
    text = block[hash_count + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{hash_count}", children)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])
        
