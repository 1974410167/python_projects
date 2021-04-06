import random

def guess_number():

    t1 = 1
    while t1 == 1:
        print('--------------')
        print('1. 简单')
        print('2. 一般')
        print('3. 困难')
        print('--------------')

        t = input("输入你想玩的游戏难度代号:")

        n = 0
        if t == '1':
            n = 8
        elif t == '2':
            n = 5
        elif t == '3':
            n = 3
        else:
            print('请输入有效数字！')

        target = random.randint(0, 100)

        m = 0

        while m<n:
            number = int(input("输入所猜数字(0-100):"))
            if number<target:
                print('猜小了！')
            elif number>target:
                print('猜大了！')
            else:
                print('-------------------')
                print('猜对了，游戏胜利！')
                print(f'用了{m+1}次机会！')
                break
            m += 1
            if m == n:
                print('-------------------')
                print(f'{m}次机会已经用完！')
                print('游戏失败！')
                break
        print('-----------------')
        print('是否继续游戏？')
        print('1. 继续')
        print('2. 结束')

        t1 = int(input('是否继续游戏:'))


if __name__ == '__main__':
    guess_number()


