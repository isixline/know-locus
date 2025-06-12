import re
from core.config import link_pattern

def remove_links(content: str) -> str:
    text = re.sub(link_pattern, "", content)

    return text