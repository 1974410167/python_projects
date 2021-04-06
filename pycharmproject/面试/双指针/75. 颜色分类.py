from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)

        if l == 1:
            return nums

        p0 = 0
        p2 = l - 1
        i = 0
        while i <= p2:

            while nums[i] == 2 and i <= p2:

                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1

            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1

            i += 1
        return nums

nums = [2,0,2,1,1,0]
S = Solution()
a = S.sortColors(nums)
print(a)