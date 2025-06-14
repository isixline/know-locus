from sentence_transformers import SentenceTransformer
from utils.faiss_matcher import match_by_faiss
from utils.sentence_matcher import match_by_sentence
from utils.timers import track_time

@track_time
def match(query, corpus, top=5):
    # 加载预训练模型（推荐这个：小巧，速度快，效果不错）
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 编码
    corpus_vector = model.encode([item["text"] for item in corpus])
    query_vector = model.encode(query)

    # 查询
    results = match_by_sentence(query_vector, corpus_vector, top)
    for result in results:
        result["text"] = corpus[result["index"]]["text"]
        result["name"] = corpus[result["index"]]["name"]
        result["score"] = result["score"]
    return results



     
