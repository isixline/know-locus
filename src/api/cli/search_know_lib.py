from core.match import search_files_in_know_lib

def show_results(results):
    for result in results:
        print(f"Name: {result['name']}, Score: {result['score']}")
        print(f"Text: {result['text'][:100]}...")  # 只显示前100个字符
        print("-" * 40)

if __name__ == "__main__":
    import core.filter
    file_filter = core.filter.ieda_notes_filter
    query = input("请输入查询内容: ")
    results = search_files_in_know_lib(query, file_filter)
    show_results(results)