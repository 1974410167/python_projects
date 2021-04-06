target = 5

nums = [2,5,77,222,333,4444,22222]
class Solution:
    def binary_search(t,nums):

        left = 0
        right = len(nums)
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>t:
                right = mid - 1
            elif nums[mid] == t:
                return mid
            else:
                left = mid + 1
        return -1


def binary_search1(t,nums,right,left):



    mid = (right+left)//2

    if nums[mid] > t:
        right = mid - 1
        return binary_search1(t,nums,right,left)
    elif nums[mid] == t:
        return mid
    else:
        left = mid + 1
        return binary_search1(t,nums,right,left)

aa = binary_search1(target,nums,7,0)
print(aa)
