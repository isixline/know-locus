from sentence_transformers import SentenceTransformer
from utils.timers import track_time
from functools import lru_cache

@lru_cache(maxsize=2)
def get_model(name="all-MiniLM-L6-v2"):
    return SentenceTransformer(name)

@track_time
def vectorized_corpus(get_corpus: callable):
    corpus_vector = get_model().encode(get_corpus(), batch_size=64, show_progress_bar=True)
    return corpus_vector


@track_time
def vectorize_text(text: str):
    text_vector = get_model().encode(text)
    return text_vector
