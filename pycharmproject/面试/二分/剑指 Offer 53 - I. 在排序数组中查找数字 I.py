from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)


nums = [5,7,7,8,8,8]
target = 8

s = Solution()
q = s.search(nums,target)
print(q)

