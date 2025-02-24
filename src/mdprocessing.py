import re
import parentnode
import textnode
import leafnode
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

def markdown_to_HTMLNode(markdown: str) -> parentnode.ParentNode:
    body = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_BlockType(block)
        match block_type:
            case BlockType.PARAGRAPH:
                body.extend(handle_text_block(block))
            case BlockType.HEADING:
                body.append(handle_heading_block(block))
            case BlockType.CODE:
                body.append(handle_code_block(block))
            case BlockType.QUOTE:
                body.append(handle_quote_block(block))
            case BlockType.UNORDERED_LIST:
                body.append(handle_ulist_block(block))
            case BlockType.ORDERED_LIST:
                body.append(handle_olist_block(block))
    return parentnode.ParentNode(tag = "body", children = body)

def handle_text_block(block: str) -> list[leafnode.LeafNode]:
    htmlnodes = []
    textnodes = textnode.markdown_to_TextNodes(block)
    for tn in textnodes:
        htmlnodes.append(tn.to_HTMLNode())
    return htmlnodes

def handle_heading_block(block: str) -> parentnode.ParentNode:
    block_split = block.split(" ", maxsplit=1)
    num_hashtag = len(block_split[0])
    text = block_split[1]
    children = handle_text_block(text)
    return parentnode.ParentNode(tag = f"h{num_hashtag}", children = children)

def handle_code_block(block: str) -> parentnode.ParentNode:
    code = leafnode.LeafNode(tag = "code", value = block.strip("`"))
    return parentnode.ParentNode(tag = "pre", children = [code])

def handle_quote_block(block: str) -> leafnode.LeafNode:
    text = block.split(">", maxsplit=1)[1]
    return leafnode.LeafNode(tag = "blockquote", value = text)

def handle_ulist_block(block: str) -> parentnode.ParentNode:
    list_items = []
    list_item_texts = [text.split("-", maxsplit=1) for text in block.split("\n")]
    for item in list_item_texts:
        list_items.append(leafnode.LeafNode(tag = "li", value = item[1]))
    return parentnode.ParentNode(tag = "ul", children = list_items)

def handle_olist_block(block: str) -> parentnode.ParentNode:
    list_items = []
    list_item_texts = [text.split(".", maxsplit=1) for text in block.split("\n")]
    for item in list_item_texts:
        list_items.append(leafnode.LeafNode(tag = "li", value = item[1]))
    return parentnode.ParentNode(tag = "ol", children = list_items)