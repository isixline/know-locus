import os
import pickle
from config.env import get_vector_cache_path


def use_vector_cache(genera_cache: callable):
    vector_cache_path = get_vector_cache_path() 
    if os.path.exists(vector_cache_path):
        with open(vector_cache_path, "rb") as f:
            corpus_vector = pickle.load(f)
    else:
        corpus_vector = genera_cache()
        with open(vector_cache_path, "wb") as f:
            pickle.dump(corpus_vector, f)
    return corpus_vector

def clear_vector_cache():
    vector_cache_path = get_vector_cache_path() 
    if os.path.exists(vector_cache_path):
        os.remove(vector_cache_path)
        print(f"clear cache: {vector_cache_path}")
    else:
        print("cache not found, nothing to clear.")