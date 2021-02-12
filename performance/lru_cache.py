import time
from functools import lru_cache

@lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(10)
    return 'Input was {}'.format(input)
