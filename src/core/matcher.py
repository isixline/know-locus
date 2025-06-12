from sentence_transformers import SentenceTransformer
from sentence_transformers import util

def match_by_sentence_transformers(query, corpus):
    """
    使用 Sentence Transformers 进行句子匹配
    :param query: 查询句子
    :param corpus: 语料库句子列表
    :return: 与查询最相似的句子及其相似度{text: 句子, score: 相似度}
    """
    # 加载预训练模型（推荐这个：小巧，速度快，效果不错）
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 编码
    query_embedding = model.encode(query)
    corpus_embeddings = model.encode(corpus)

    # 找到最相似的句子
    cos_scores = util.cos_sim(query_embedding, corpus_embeddings)

    # 排序
    top_result = sorted(zip(corpus, cos_scores[0]), key=lambda x: x[1], reverse=True)

    # 返回最相似的句子和相似度
    result = [{"text": sentence, "score": score.item()} for sentence, score in top_result]

    return result