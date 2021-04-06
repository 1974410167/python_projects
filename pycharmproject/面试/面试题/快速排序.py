def quick_sort(nums):

    l = len(nums)

    if l<2:
        return nums

    sign = nums[0]
    nums = nums[1:]

    left = []
    right = []
    for i in nums:
        if i>sign:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left)+[sign]+quick_sort(right)

