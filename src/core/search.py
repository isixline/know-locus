from utils.file_loader import read_files
from utils.link_parser import parse_links_and_content

def search_files(root_dir, file_filter):
    """
    在指定目录下的所有文件中搜索 [[xxx]] 格式的链接内容。

    参数:
        root_dir (str): 根目录路径
        file_filter (fun): 文件过滤器函数，接收文件名作为参数，返回布尔值
    返回:
        List[Dict[str, Any]]: [{ "name": 文件名, "links": 链接列表, "text": 原始文本 }, ...]
    """
    files = read_files(root_dir, file_filter)
    results = []

    for file in files:
        content = file["content"]
        parsed = parse_links_and_content(content)
        results.append({
            "name": file["name"][:-3],  # 去掉后缀
            "links": parsed["links"],
            "text": parsed["text"]
        })

    return results

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os   

    load_dotenv()  # 默认读取 .env 文件
    root_dir = os.getenv('KNOW_LIB_FILE_PATH')
    # 过滤 md 文件并且以数字开头
    file_filter = lambda filename: filename.endswith('.md') and filename[0].isdigit()
    results = search_files(root_dir, file_filter)
    for result in results:
        print(f"File: {result['name']}")
        print(f"Links: {result['links']}")
        print(f"Text: {result['text'][:100]}...")  # Print first 100 characters of text
        print()