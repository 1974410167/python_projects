def ab(num):
    if len(num) >= 2:
        L = len(num)
        mid = num[L // 2]
        left, right = [], []
        num.remove(mid)
        for i in num:
            if mid >= i:
                left.append(i)
            else:
                right.append(i)
        return ab(left) + [mid] + ab(right)
    else:
        return num


