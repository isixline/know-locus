from dotenv import load_dotenv
import os

load_dotenv()   

def get_vector_cache_path():
    return os.getenv('VECTOR_CACHE_PATH')

def get_know_lib_path():
    return os.getenv('KNOW_LIB_PATH')
