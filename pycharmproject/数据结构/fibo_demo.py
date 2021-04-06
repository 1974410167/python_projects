from clockedeco2 import clock
import time
import functools
@clock
@functools.lru_cache()
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

if __name__=="__main__":
    t1=time.time()
    print(fibonacci(100))
    print(time.time()-t1)