import os

def read_files(root_dir, file_filter):
    """
    递归遍历 root_dir，读取经file_filter的文件内容。
    
    参数:
        root_dir (str): 根目录路径
        file_filter (fun): 文件过滤器函数，接收文件名作为参数，返回布尔值
    
    返回:
        List[Dict[str, str]]: [{ "name": 文件名, "content": 文件内容 }, ...]
    """
    results = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if file_filter(filename):
                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, root_dir)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    results.append({
                        "name": filename,
                        "content": content
                    })
                except Exception as e:
                    print(f"读取失败：{relative_path}，错误：{e}")

    return results
