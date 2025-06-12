from sentence_transformers import SentenceTransformer
from sentence_transformers import util


print("加载模型...")

# 加载预训练模型（推荐这个：小巧，速度快，效果不错）
model = SentenceTransformer('all-MiniLM-L6-v2')

print("模型加载完成！")

query = "我喜欢看电影"
corpus = ["我爱看电影", "我在跑步", "我今天不开心", "我很喜欢动漫"]

# 编码
query_embedding = model.encode(query)
corpus_embeddings = model.encode(corpus)

# 找到最相似的句子
cos_scores = util.cos_sim(query_embedding, corpus_embeddings)

# 排序
top_result = sorted(zip(corpus, cos_scores[0]), key=lambda x: x[1], reverse=True)

print("与查询最相似的句子是：")
for sentence, score in top_result:
    print(f" - {sentence} (相似度: {score:.4f})")