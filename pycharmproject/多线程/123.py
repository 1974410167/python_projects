a=input()
a=int(a)
if a%100==0:
    if a%400==0:
        print("是闰年")
    else:
        print("不是闰年")
else:
    if a%4==0:
        print("是闰年")
    else:
        print("不是闰年")
