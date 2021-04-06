from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time
def task(n):
    print('%s is running' %os.getpid())
    time.sleep(2)
    return n**2


if __name__ == '__main__':
    # p=ProcessPoolExecutor(2)
    p=ThreadPoolExecutor(3)
    start = time.time()
    obj=p.map(task,range(10))
    p.shutdown()
    print('='*30)
    print(list(obj))
    print(time.time() - start)