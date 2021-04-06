import threading
import time
#这个程序会出现共享变量问题，两个函数同时使用sum变量
#会出现问题
cache = 5

cache_list = []

str_stu = "abcdefgh"

stu = list(str_stu)


def add():
    global cache_list,stu
    while True:
        if len(stu)==0:
            break
        if len(cache_list) <= cache-1:
            t = stu.pop()
            cache_list.append(t)
        time.sleep(2)

def minu():
    global cache_list,stu

    while True:
        if len(cache_list)==0 and len(stu)==0:
            break
        else:
            cache_list.remove(cache_list[-1])
        time.sleep(2)

if __name__=="__main__":

    t1 = threading.Thread(target=add, args=())
    t2 = threading.Thread(target=minu, args=())



    while t1.is_alive() or t2.is_alive():
        print(f"stu       ======>>> {stu}")
        print(f"cache_list======>>> {cache_list}")
        time.sleep(2)


