

def bubble_sort(num):
    l = len(num)
    for i in range(l-1):
        for j in range(i+1,l):
            if num[i]>num[j]:
                num[i],num[j] = num[j],num[i]

    return num


l = [i for i in range(10)]
import random

random.shuffle(l)

print(l)

a = bubble_sort(l)

print(a)