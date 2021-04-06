

def mergeSort(num):

    L = len(num)
    if L<2:
        return num
    mid = L//2

    left = mergeSort(num[:mid])
    right = mergeSort(num[mid:])

    result = []
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result

# 时间复杂度O(nlog2n)
#

list_num = [3,7,6,8,9,2,4]


print(mergeSort(list_num))

