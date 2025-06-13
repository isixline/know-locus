from utils.file_loader import read_files
from core.matcher import match
from dotenv import load_dotenv
import os   
from core.formatter import remove_links

load_dotenv() 

def search_files(query, root_dir, file_filter):
    files = read_files(root_dir, file_filter)
    parsed_files = []

    for file in files:
        content = file["content"]
        parsed_files.append({
            "name": file["name"][:-3],  # 去掉后缀
            "text": remove_links(content),  # 移除链接
        })

    # 使用 sentence_transformers 进行匹配
    results = match(query, parsed_files)

    return results

def search_files_in_know_lib(query, file_filter):
    root_dir = os.getenv('KNOW_LIB_FILE_PATH')

    return search_files(query, root_dir, file_filter)

def show_results(results):
    for result in results:
        print(f"Name: {result['name']}, Score: {result['score']}")
        print(f"Text: {result['text'][:100]}...")  # 只显示前100个字符
        print("-" * 40)

if __name__ == "__main__":
    import core.filter
    file_filter = core.filter.inspiration_notes_filter
    query = input("请输入查询内容: ")
    results = search_files_in_know_lib(query, file_filter)
    show_results(results)
   