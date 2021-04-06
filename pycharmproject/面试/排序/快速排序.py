
list_num = [3,22,1,3452,223,11]

def QuickSort(list):

    l = len(list)
    if l<2:
        return list

    left,right = [],[]
    mid = list[0]
    list = list[1:]

    for i in list:
        if i>mid:
            right.append(i)
        else:
            left.append(i)

    return QuickSort(left)+[mid]+QuickSort(right)

# 当n较大时，是所有内部排序方法速度最快的一种
# 时间复杂度O(n log2n)


def quickly(nums):

    l = len(nums)

    if l<2:
        return nums

    mid = nums[0]
    left,right = [],[]
    nums = nums[1:]

    for i in nums:
        if i>mid:
            right.append(i)
        else:
            left.append(i)

    return quickly(left)+[mid]+quickly(right)


a = quickly(list_num)
print(a)








# 迭代法
def f2(num):

    l = len(num)
    if l <= 1:
        return num

    stack = [num]

    result = []
    while stack:

        t = stack.pop(0)

        l = len(t)
        if l==0:
            continue

        if l==1:
            result.append(t[0])
            continue

        k = t[0]
        num = t[1:]
        left,right = [],[]

        for i in num:
            if i > k:
                right.append(i)
            else:
                left.append(i)

        stack.insert(0,left)
        stack.insert(1,[k])
        stack.insert(2,right)

    return result



















