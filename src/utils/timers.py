import time
from functools import wraps

def track_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Timers] {func.__name__} ran in {(end - start):.4f}s")
        return result
    return wrapper
