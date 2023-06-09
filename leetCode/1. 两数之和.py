from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = dict()
        i = 0
        while i < len(nums):
            dict1[nums[i]] = i
            i += 1

        j = 0
        while j < len(nums):
            t = target - nums[j]
            if t in dict1:
                index = dict1[t]
                if index != j:
                    return [dict1[t], j]
            j += 1

s = Solution()
q = s.twoSum([1,3,4,2],6)
print(q)