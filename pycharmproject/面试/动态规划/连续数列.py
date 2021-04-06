num = [-2,1,-3,4,-1,2,1,-5,4]



def ss(num):
    for i in range(1,len(num)):
        num[i] = max(num[i]+num[i-1],num[i])
    return max(num)

print(ss(num))