from sentence_transformers import util
from utils.timers import track_time

@track_time
def match_by_sentence(query_vector, corpus_vector, top):
    # 找到最相似的句子
    cos_scores = util.cos_sim(query_vector, corpus_vector)
    # 排序
    top_indices = cos_scores[0].argsort(descending=True)[:top]
    # 返回结果
    results = []
    for idx in top_indices:
        results.append({
            "index": idx.item(),
            "score": cos_scores[0][idx].item()
        })
    return results


     
