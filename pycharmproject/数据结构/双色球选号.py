import random

# 定义函数，得到一注号码
def get_number():
    list = []
    for i in range(6):

        # 红色球，从1-33中随机一个
        t = random.randint(1,33)
        list.append(t)

    # 蓝色球，从1--16随机一个
    m = random.randint(1,16)
    list.append(m)
    return list

# 定义函数，想要得到几注号码，即调用几次get_number()
def main():

    t = 1
    while t==1:

        # 输入数字，人工选择几注号码
        m = int(input('你想机选几注号码？:'))

        for j in range(m):
            a = get_number()
            for i in range(len(a)):
                if i == 6:
                    print('|',end=' ')
                print('%02d' % a[i] ,end=' ')
            print()

        print('-----------------')
        print('是否继续选号？')
        print('1.继续')
        print('2.结束')

        t = int(input("输入1或2:"))

# 程序入口，调用函数
if __name__ == '__main__':
    main()