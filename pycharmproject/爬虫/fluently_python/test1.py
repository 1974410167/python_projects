


a = [0,1]
import time
print("你的内存即将爆炸！！！！！！")
while True:
    t = a[-1]+a[-2]
    a.append(t)
    if len(a) == 100:
        break