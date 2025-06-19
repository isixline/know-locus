from sentence_transformers import SentenceTransformer
from utils.timers import track_time

# 加载预训练模型（推荐这个：小巧，速度快，效果不错）
model = SentenceTransformer("all-MiniLM-L6-v2")


@track_time
def vectorized_corpus(get_corpus: callable):
    corpus_vector = model.encode(get_corpus(), batch_size=64, show_progress_bar=True)
    return corpus_vector


@track_time
def vectorize_text(query: str):
    query_vector = model.encode(query)

    return query_vector
