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