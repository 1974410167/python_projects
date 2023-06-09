from typing import List

nums = [-2,1]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max1 = nums[0]
        pre = nums[0]
        index = 1
        l = len(nums)
        while index < l:
            if pre > 0:
                pre = pre + nums[index]
            else:
                pre = nums[index]
            if pre > max1:
                max1 = pre
            index += 1
        return max1

s = Solution()
q = s.maxSubArray(nums)
print(q)
