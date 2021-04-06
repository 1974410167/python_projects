
    
from fluently_python import decoration1
from inspect import getgeneratorstate

def si_po1(a):
    print("->co started a= ",a)
    b = yield a
    print("-> co re",b)
    c = yield a + b
    print("-> re co" ,c)

# 计算移动平均值
@decoration1.coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

a=averager()
print(getgeneratorstate(a))
print(a.send(10))
print(a.send(100))
print(a.send(20))


