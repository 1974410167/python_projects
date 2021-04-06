from time import time,sleep
from threading import Thread
#执行用时4S
def loop1():
    sleep(4)
    print("loop1结束")
def loop2():
    sleep(2)
    print("loop2结束")
def main():
    start=time()
    p1=Thread(target=loop1,args=())
    p1.start()
    p2 = Thread(target=loop2, args=())
    p2.start()
    p1.join()
    p2.join()
    end=time()
    print("主程序耗时%.2f秒"%(end-start))
if __name__=="__main__":
    main()
    while True:
        sleep(1)

