from utils.file_loader import read_files
from core.matcher import match
from core.formatter import remove_links
from config.env import get_know_lib_path

def search_in_files(query, root_dir, file_filter):
    files = read_files(root_dir, file_filter)
    parsed_files = []

    for file in files:
        content = file["content"]
        parsed_files.append({
            "name": file["name"][:-3],  # 去掉后缀
            "text": remove_links(content),  # 移除链接
        })

    results = match(query, parsed_files)

    return results

def search_files_in_know_lib(query, file_filter):
    know_lib_path = get_know_lib_path()
    return search_in_files(query, know_lib_path, file_filter)
