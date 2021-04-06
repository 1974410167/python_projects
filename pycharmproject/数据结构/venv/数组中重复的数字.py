
list = [2,3,1,0,2,5]
# def repeat_1(list):


def repeat_2(list):
    L = len(list)
    for i in range(L):
        if list[i]!=i:
            list[list[i]],list[i]=list[i],list[list[i]]

        else:
            return list[i]

def duplicate(numbers,duplication):
    # write code here
    if numbers is None or len(numbers) == 0:
        return False
    for i in numbers:
        if i < 0 or i >= len(numbers):
            return False
    for i in range(len(numbers)):
        while i != numbers[i]:
            if numbers[i] == numbers[numbers[i]]:
                duplication[0] = numbers[i]
                return True
            tmp = numbers[numbers[i]]
            numbers[numbers[i]] = numbers[i]
            numbers[i] = tmp
    return False
# repeat_2(list)

duplicate(numbers=list,duplication=dict())