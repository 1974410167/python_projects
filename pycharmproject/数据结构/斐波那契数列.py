def fib(n):
    nums = [0, 1]
    if n <= 1:
        return n
    t = 2
    while t <= n:
        target = nums[0] + nums[1]
        nums[0] = nums[1]
        nums[1] = target
        t += 1


    tt = 1*10**9+7

    print(tt)

    print(target)

    if target<tt:
        target = target%tt
    else:
        target = target//tt

    return target


print(fib(6))

print(134903163)