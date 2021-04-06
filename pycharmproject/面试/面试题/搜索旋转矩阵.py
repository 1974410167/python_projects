def search(nums, target):
    if not nums:
        return False

    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True

        if nums[mid] >= nums[l]:
            if nums[l] < target < nums[mid]:
                r = mid - 1
                if nums[l] == target:
                    return True
            else:
                l = mid + 1
        else:
            if nums[mid] < target < nums[r]:
                l = mid + 1
                if nums[r] == target:
                    return True
            else:
                r = mid - 1
    return False

nums = [1,0,1,1,1]
target = 0


a = search(nums,target)
print(a)