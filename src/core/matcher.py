from utils.faiss_matcher import match_by_faiss
from utils.sentence_matcher import match_by_sentence
from utils.timers import track_time
from utils.vectorizer import vectorize_text, vectorized_corpus
from utils.file_loader import read_files
from core.formatter import remove_links, remove_blank_dash_lines


@track_time
def match(query, corpus, top=5):
    get_corpus = lambda: [
        {"text": item["text"], "name": item["name"]} for item in corpus
    ]
    corpus_vector = vectorized_corpus(get_corpus)
    query_vector = vectorize_text(query)

    # 查询
    match_results = match_by_faiss(query_vector, corpus_vector, top)

    # 整理
    results = []
    for match_result in match_results:
        result = {
            "text": corpus[match_result["index"]]["text"],
            "name": corpus[match_result["index"]]["name"],
            "score": float(match_result["score"]),
        }
        results.append(result)

    return results


@track_time
def match_in_files(query, root_dir, file_filter, top):
    files = read_files(root_dir, file_filter)
    parsed_files = []

    for file in files:
        content = file["content"]
        parsed_files.append(
            {
                "name": file["name"][:-3],  # 去掉后缀
                "text": remove_blank_dash_lines(remove_links(content)),  # 移除链接
            }
        )

    results = match(query, parsed_files, top)

    return results
