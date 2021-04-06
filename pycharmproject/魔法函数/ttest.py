
list1 = [1,3,3,4,4,5,5,7,7,7,6,5,4,2,2]

def sort_1(num):

    l = len(num)
    i = 0
    j = l - 1
    res = []

    if num[i]<=num[j]:
        res.append(num[i])
        i += 1
    else:
        res.append(num[j])
        j-=1

    while i<j:

        if num[i]<=num[j]:
            if res and res[-1]!=num[i]:
                res.append(num[i])
                i += 1
            else:
                while res and res[-1]==num[i]:
                    i += 1

        else:
            if res and res[-1]!=num[j]:
                res.append(num[j])
                j -= 1
            else:
                while res and res[-1]==num[j]:
                    j-=1

    return res
s = sort_1(list1)
print(s)



