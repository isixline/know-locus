import faiss
import numpy as np
from utils.timers import track_time

@track_time
def match_by_faiss(query_vector, corpus_vector, top):

    # 编码
    corpus_vector = np.array(corpus_vector).astype("float32")


    # 构建 FAISS 索引
    index = faiss.IndexFlatL2(corpus_vector.shape[1])  # 使用 L2 距离
    index.add(corpus_vector)  # 加入向量

    # 查询
    query_vector = np.array([query_vector]).astype("float32")
    distances, indices = index.search(query_vector, k=top)  # 找到最相似的5个

    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "index": idx,
            "score": 1 - distances[0][i]  # 将距离转换为相似度
        })
    return results




     
