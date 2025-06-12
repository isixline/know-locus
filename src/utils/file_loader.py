import os

def read_files_with_suffix(root_dir, suffix=".md"):
    """
    递归遍历 root_dir，读取所有以 suffix 结尾的文件内容。
    
    参数:
        root_dir (str): 根目录路径
        suffix (str): 文件后缀名（默认 ".md"）
    
    返回:
        List[Dict[str, str]]: [{ "name": 相对路径或文件名, "content": 文件内容 }, ...]
    """
    results = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(suffix):
                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, root_dir)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    results.append({
                        "name": relative_path,
                        "content": content
                    })
                except Exception as e:
                    print(f"读取失败：{relative_path}，错误：{e}")

    return results
