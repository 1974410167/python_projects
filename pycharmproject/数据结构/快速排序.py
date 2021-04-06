
def quick_sort_1(num):

    if len(num)<2:
        return num

    left,right = [],[]
    mid = num[0]
    num = num[1:]

    for i in num:
        if i>mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort_1(left)+[mid]+quick_sort_1(right)




import random
l = [i for i in range(10)]
random.shuffle(l)
print(l)
s = quick_sort(l)
print(s)