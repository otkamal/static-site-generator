import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 0
    HEADING = 1
    CODE = 2
    QUOTE = 3
    UNORDERED_LIST = 4
    ORDERED_LIST = 5

def markdown_to_blocks(markdown: str) -> list[str]:
    if not markdown:
        return []
    
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: len(x) > 0, blocks))
    return blocks

def block_to_BlockType(block_text: str) -> BlockType:
    
    REGEX_HEADING = r"^(#{1,6})\s+(.*)$"
    REGEX_CODE_BLOCK = r"(`{3,})\n?([\s\S]*?)*?\n?\1$"
    REGEX_QUOTE = r"^(>\s?)(.*)$"
    REGEX_UNORDERED_LIST = r"^([*-])\s+(.*)$"
    REGEX_ORDERED_LIST = r"(\d+)\.\s+(.*)$"

    REGEX_TO_BLOCKTYPE = {
        REGEX_HEADING: BlockType.HEADING,
        REGEX_CODE_BLOCK: BlockType.CODE,
        REGEX_QUOTE: BlockType.QUOTE,
        REGEX_UNORDERED_LIST: BlockType.UNORDERED_LIST,
        REGEX_ORDERED_LIST: BlockType.ORDERED_LIST
    }

    for regex in REGEX_TO_BLOCKTYPE.keys():
        if re.match(regex, block_text):
            return REGEX_TO_BLOCKTYPE[regex]

    is_unordered_list = True
    for line in block_text.split("\n"):
        if not re.match(REGEX_UNORDERED_LIST, line):
            is_unordered_list = False
            break
    
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    
    # need to finished ordered_list implementation
    is_ordered_list = True
    item_number = 1
    for line in block_text.split("\n"):
        if not re.match(REGEX_ORDERED_LIST, line):
            is_ordered_list = False
            break

        if not line.startswith(f"{item_number}."):
            is_ordered_list = False
            break
        item_number += 1


    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH