import time
import threading
#多线程传入参数
#用join()来等待程序完成
def loop1(x):
    print("loop1当前时间:",time.ctime())
    print("loop1的参数：",x)
    time.sleep(4)
    print("loop1结束的时间：",time.ctime())
def loop2(y,z):
    print("loop2当前时间：",time.ctime())
    print("loop2的参数：",y,z,"\n")
    time.sleep(2)
    print("loop2结束的时间：",time.ctime())
def main():
    print("主程序开始的时间：",time.ctime())

    t1=threading.Thread(target=loop1,args=("哈哈哈",))
    t1.start()
    a = threading.enumerate

    t2=threading.Thread(target=loop2,args=("嘻嘻嘻","啦啦啦"))
    t2.start()
    a=threading.enumerate
    print("主程序结束的时间：",time.ctime())
    print(a)
    threading.activeCount
if __name__=="__main__":
    main()
    time.sleep(4)