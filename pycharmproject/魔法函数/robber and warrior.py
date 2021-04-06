robber = [5, 4]
warrior = [7, 8, 4]
robber1 = [5, 5]
warrior1 = [12]
def robber_and_warrior(robber,warrior):
    res = "King will die"

    l = len(robber)
    l1 = len(warrior)

    if l>l1:
        return res

    robber = sorted(robber)
    warrior = sorted(warrior)

    i,j = 0,0

    res1 = 0
    while i<=l-1 and j<=l1-1:

        if robber[i]<warrior[j]:
            res1 += warrior[j]
            i += 1
            j += 1
        else:
            j += 1

    if i>l-1:
        return res1
    else:
        return res

q = robber_and_warrior(robber,warrior)
print(q)