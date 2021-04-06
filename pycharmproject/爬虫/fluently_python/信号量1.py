import threading
import random
import time

# P,Q缓冲区
m = 10
# Q,R缓冲区
n = 10

# 缓冲区
s1 = threading.BoundedSemaphore(m)
s2 = threading.BoundedSemaphore(n)
# 定义P行为，
def fun_P():

    s1.acquire()     # 从输入设备读入信息，传给Q，PQ缓冲区减一
    print('》》PQ减一')
    time.sleep(1)

def fun_Q_s1():

    if s1._value < m:    # 判断m缓冲区有没有数据，有数据拿走
        s1.release()     # Q从PQ缓冲区拿数据，PQ缓冲区加一
        print(f'》》PQ加一')
        time.sleep(1)
    else:
        return

    s2.acquire()     # Q加工数据后传入QR缓冲区，QR缓冲区减一
    print('》》RQ减一')
    time.sleep(1)

def fun_R():

    if s2._value < n:     # 判断n缓冲区有没有数据，有数据拿走
        s2.release()      # 拿到QR缓冲区数据，QR缓冲区加一
        print(f'》》PQ加一')
        time.sleep(1)
    else:
        return

if __name__ =="__main__":

    while True:

        thread_target1 = threading.Thread(target=fun_P,args=())
        thread_target2 = threading.Thread(target=fun_Q_s1,args=())
        thread_target3 = threading.Thread(target=fun_R,args=())
        thread_target1.start()
        thread_target2.start()
        thread_target3.start()

        time.sleep(2)         # 以免启动过多线程
