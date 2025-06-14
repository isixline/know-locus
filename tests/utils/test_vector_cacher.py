import os
import pickle
from utils.vector_cacher import use_vector_cache, clear_vector_cache

vector_cache_path = "tests/data/test_vector_cache.pkl"

def test_use_vector_cache(monkeypatch):
    # 设置环境变量
    monkeypatch.setenv("VECTOR_CACHE_PATH", vector_cache_path)

    # 清除缓存文件
    clear_vector_cache()

    # 模拟生成向量的函数
    def mock_genera_cache():
        return [1.0, 2.0, 3.0]

    # 使用缓存
    vectors = use_vector_cache(mock_genera_cache)
    
    # 检查缓存文件是否创建
    assert os.path.exists(vector_cache_path)

    # 检查返回的向量是否正确
    assert vectors == [1.0, 2.0, 3.0]

    # 清除缓存文件
    clear_vector_cache()

def test_clear_vector_cache(monkeypatch):
    # 设置环境变量
    monkeypatch.setenv("VECTOR_CACHE_PATH", vector_cache_path)

    # 创建一个空的缓存文件
    with open(vector_cache_path, "wb") as f:
        pickle.dump([], f)

    # 清除缓存
    clear_vector_cache()

    # 检查缓存文件是否被删除
    assert not os.path.exists(vector_cache_path)