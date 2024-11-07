from enum import Enum
from textnode import *
from htmlnode import *

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
            return 'heading'
    elif text.startswith('```') and text.endswith('```'):
        return 'code'
    elif all(line.startswith('>') for line in text.split('\n')):
        return 'quote'
    elif all((line.startswith('*') and line[1] == ' ') or (line.startswith('-') and line[1] == ' ') for line in text.split('\n')):
        return 'unordered_list'
    elif all(line[0].isdigit() and int(line[0]) == (i + 1) and line[1] == '.' and line[2] == ' ' for i, line in enumerate(text.split('\n'))):
        return 'ordered_list'

