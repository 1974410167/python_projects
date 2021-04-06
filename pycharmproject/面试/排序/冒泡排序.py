
list_num = [3,22,1,3452,223,11]



def Bobble_Sort(list):
    l = len(list)
    for i in range(l-1):
        for j in range(i+1,l):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    return list

# 稳定排序
# 可用于链式结构
# 时间复杂度O(n2)


s = Bobble_Sort(list_num)
print(s)
