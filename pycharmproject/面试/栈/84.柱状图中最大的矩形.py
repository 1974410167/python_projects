
s = [10,9,2,5,3,4]

def lenthOfLIS(list):

    L = len(list)
    if not L:
        return 0
    if L==1:
        return 1
    result_max = 0
    for i in range(L-1):
        Max = 1
        t = list[i]
        for j in range(i+1,L):
            if list[j]>t:
                Max = Max+1
                t = list[j]

        result_max = max(result_max,Max)

    return result_max

s = lenthOfLIS(s)
print(s)