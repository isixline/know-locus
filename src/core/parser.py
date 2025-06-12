import re
from core.config import link_pattern

def parse_links(content: str) -> list:
    links = re.findall(link_pattern, content)
    return links