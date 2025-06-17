def know_lib_filter(filename: str) -> bool:
    return filename.endswith('.md')

def idea_notes_filter(filename: str) -> bool:
    return filename.endswith('.md') and filename[0].isdigit()

def tech_notes_filter(filename: str) -> bool:
    return filename.endswith('.md') and filename.startswith('🛠️')