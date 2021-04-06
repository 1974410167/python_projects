def SumMultiplier(arr):

  # code goes here
    if len(arr)<2:
        return False
    t = sum(arr)*2
    max = 0
    for i in arr:
        if i*max>t:
            return True
        else:
            max = max if max>i else i

    return False

s = [1,2,10,3,1,12]

# print(SumMultiplier(arr=s))

str = 'bcab'

def StringReduction(str):

    if len(set(str))!=1:
        L = len(str)
        num = {'a','b','c'}
        for i in range(L-1):
            if str[i]!=str[i+1]:
                for j in num:
                    if j!=str[i] and j!=str[i+1]:

                        str = str[0:i]+j+str[i+2:]

                        return StringReduction(str)
    else:
        return len(str)
    
aa = StringReduction('cab')
print(aa)