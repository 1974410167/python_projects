


def Statistical_results():

    m = 1
    while m==1:

        print('请依次输入学生成绩(结束输入键入quit):')

        target = ''

        # 存放学生成绩
        nums = []

        # 序号，从1开始
        n = 1

        while True:

            # 输入成绩
            target = input(f'{n}.')

            # 键入quit,结束输入
            if target=='quit':
                break

            target = int(target)

            nums.append(target)
            n += 1

        s1 = sum(nums)

        # 分别计算出成绩总和，平均数，最好成绩，最坏成绩
        print(f'成绩总和:{s1}')
        print(f'平均数:{s1/len(nums)}')
        print(f'最好成绩:{max(nums)}')
        print(f'最差成绩:{min(nums)}')

        print('-----------------')
        print('是否继续？')
        print('1. 继续')
        print('2. 结束')

        m = int(input('是否继续:'))

Statistical_results()