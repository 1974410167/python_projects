import time
#执行用时6S
def loop1():
    print("loop1当前时间:",time.ctime())
    time.sleep(4)
    print("loop1结束的时间：",time.ctime())
def loop2():
    print("loop2当前时间：",time.ctime())
    time.sleep(2)
    print("loop2结束的时间：",time.ctime())
def main():
    loop1()
    print("******************")
    loop2()
a=main()
print(a)



