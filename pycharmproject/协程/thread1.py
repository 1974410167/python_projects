from concurrent.futures import ThreadPoolExecutor
import time
list = [i for i in range(1000)]

def a(t):
    while True:
        print(f"start>>>>>{t}")
        time.sleep(2)
        print(f'end>>>>>>>{t}')

if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=1000) as pool:

        s = pool.map(a,list)
        print(s)