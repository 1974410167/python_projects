
"""
输入年份，判断是否闰年。
可以根据提示，连续操作
"""


s = 1
while s == 1:
    t = False
    year = int(input('请输入年份判断是否为闰年: '))

    # 判断是否为普通年
    if year % 4 == 0:
        if year % 100 != 0:
                t = True

    # 判断是否为世纪年
    if year % 100 == 0:
        if year % 400 ==0:
            t = True

    if t == True:
        print(f"{year}是闰年")
    else:
        print(f"{year}不是闰年")

    print('-----------------')
    print('是否继续？')
    print('1. 继续')
    print('2. 结束')

    s = int(input('是否继续(输入1或2):'))
    print('-----------------')
