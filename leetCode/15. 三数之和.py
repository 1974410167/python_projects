from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = len(nums)
        i = 0
        res = []
        while i < l-2:
            left = i + 1
            right = l - 1
            if nums[i] > 0:
                return res
            while left < right:
                num = nums[i] + nums[left] + nums[right]
                if num == 0:
                    t = [nums[i], nums[left], nums[right]]
                    if t not in res:
                        res.append(t)
                    left += 1
                    right -= 1
                elif num > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
        return res

q = Solution()
c = q.threeSum([-1,0,1,2,-1,-4])
print(c)

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s2 = set()
s2.add(3)
s2.add(1)
s2.add(2)
print(s1 == s2)


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        L = len(nums)
        if L <= 2:
            return []
        res = []
        nums = sorted(nums)

        for item in range(L - 1):
            i = item + 1
            j = L - 1
            if (item > 0 and nums[item] == nums[item - 1]):
                continue

            if nums[item] > 0:
                return res

            while i < j:

                tar = nums[item] + nums[i] + nums[j]
                if tar > 0:
                    j -= 1
                elif tar < 0:
                    i += 1
                else:

                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1

                    t = []
                    t.append(nums[item])
                    t.append(nums[i])
                    t.append(nums[j])
                    res.append(t)
                    i += 1
                    j -= 1
        return res

q = Solution1()
c = q.threeSum([-1,0,1,2,-1,-4])
print(c)


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums = sorted(nums)
        res = []
        for i in range(l-2):
            target = nums[i]
            left = i+1
            right = l - 1
            while left < right:
                q = target + nums[left] + nums[right]
                if q > 0:
                    right -= 1
                elif q < 0:
                    left += 1
                else:
                    t = [nums[i], nums[left], nums[right]]
                    if t not in res:
                        res.append(t)
                    left += 1
                    right -= 1
        return res

q = Solution2()
c = q.threeSum([-1,0,1,2,-1,-4])
print(c)
