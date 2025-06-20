import re
from core.config import link_pattern

def remove_links(content: str) -> str:
    text = re.sub(link_pattern, "", content)

    return text

def remove_blank_dash_lines(content: str) -> str:
    lines = content.splitlines()
    filtered_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('-'):
            after_dash = stripped[1:]
            if after_dash.strip() == '':
                continue
        filtered_lines.append(line)
    return '\n'.join(filtered_lines)
