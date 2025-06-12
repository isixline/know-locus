from utils.file_loader import read_files
from core.matcher import match_by_sentence_transformers
from dotenv import load_dotenv
import os   
from core.formatter import remove_links

load_dotenv()  # 默认读取 .env 文件

def search_files(query, file_filter):
    root_dir = os.getenv('KNOW_LIB_FILE_PATH')

    files = read_files(root_dir, file_filter)
    parsed_files = []

    for file in files:
        content = file["content"]
        parsed_files.append({
            "name": file["name"][:-3],  # 去掉后缀
            "text": remove_links(content),  # 移除链接
        })

    # 使用 sentence_transformers 进行匹配
    results = match_by_sentence_transformers(query, parsed_files)

    return results

if __name__ == "__main__":
    import core.filter
    query = "人工智能"
    file_filter = core.filter.inspiration_notes_filter
    results = search_files(query, file_filter)
    results = [result for result in results if result["score"] > 0.5]  # 过滤低分结果
    for result in results:
        print(result)
   