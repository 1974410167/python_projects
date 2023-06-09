from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        l = len(nums)

        if l <= 1:
            return nums
        left = []
        right = []
        mid = nums[0]
        nums = nums[1:]
        for i in nums:
            if mid > i:
                left.append(i)
            else:
                right.append(i)
        return self.sortArray(left) + [mid] + self.sortArray(right)

nums = [2,3,1,4,2,5,2,3,2,4,8,9,3]
s = Solution()
q = s.sortArray(nums)
print(q)

class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:

        l = len(nums)

        if l <= 1:
            return nums

        # 基准
        t = nums[0]
        left = 0
        right = l - 1
        while left < right:
            while nums[right] < t:
                nums[0] = nums[right]
