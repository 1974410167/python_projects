import threading
#上锁，解决共享变量问题
lock=threading.Lock()#引入锁
sum=0
sums=1000000
def add():
    global sum,sums
    for i in range(sums):
        lock.acquire()#上锁
        sum=sum+1
        lock.release()#解锁
def minu():
    global sum,sums
    for i in range(sums):
        lock.acquire()  # 上锁
        sum=sum-1
        lock.release()  # 解锁
if __name__=="__main__":
    print("程序运行之前sum的值：{0}".format(sum) )
    t1=threading.Thread(target=add,args=())
    t1.start()

    t2=threading.Thread(target=minu,args=())
    t2.start()

    t1.join()
    t2.join()
    print("程序运行之后sum的值：{0}".format(sum))