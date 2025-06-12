import re

def parse_links(content: str) -> list:
    """
    提取 content 中 [[xxx]] 格式的链接内容。
    
    返回链接列表及原始文本。
    """
    # 使用正则提取 [[xxx]] 中的 xxx
    link_pattern = r"\[\[([^\[\]]+)\]\]"
    links = re.findall(link_pattern, content)

    return links
