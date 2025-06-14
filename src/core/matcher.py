from sentence_transformers import SentenceTransformer
from utils.faiss_matcher import match_by_faiss
from utils.sentence_matcher import match_by_sentence
from utils.timers import track_time
from utils.vector_cacher import use_vector_cache

@track_time
def match(query, corpus, top=5):
    # 加载预训练模型（推荐这个：小巧，速度快，效果不错）
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 编码
    genera_cache = lambda: model.encode([item["text"] for item in corpus], batch_size=64, show_progress_bar=True)
    corpus_vector = use_vector_cache(genera_cache)
    query_vector = model.encode(query)

    # 查询
    match_results = match_by_faiss(query_vector, corpus_vector, top)

    # 整理
    results = []
    for match_result in match_results:
        result = {
            "text": corpus[match_result["index"]]["text"],
            "name": corpus[match_result["index"]]["name"],
            "score": float(match_result["score"])
        }
        results.append(result)


    return results



     
