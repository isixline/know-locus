import re

def remove_links(content: str) -> str:
    """
    移除 content 中 [[xxx]] 格式的链接内容。
    
    """
    # 使用正则提取 [[xxx]] 中的 xxx
    link_pattern = r"\[\[([^\[\]]+)\]\]"

    # 移除文本中的 [[xxx]] 部分
    text = re.sub(link_pattern, "", content).strip()

    return text