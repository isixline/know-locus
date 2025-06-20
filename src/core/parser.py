import re
from core.config import link_pattern
from utils.file_loader import read_files
from core.formatter import remove_links, remove_blank_dash_lines

def parse_links(content: str) -> list:
    links = re.findall(link_pattern, content)
    return links

def parse_md(root_dir, file_filter) -> list:
    files = read_files(root_dir, file_filter)
    parsed_files = []

    for file in files:
        content = file["content"]
        parsed_files.append({
            "name": file["name"][:-3], 
            "text": remove_blank_dash_lines(remove_links(content)),
            "links": parse_links(content)
        })

    return parsed_files
