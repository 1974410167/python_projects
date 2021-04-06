
class Solution:
    def maxSubArray(self, nums):
        max1 = nums[0]
        l = len(nums)
        temp = max1
        for i in range(1, l):
            if nums[i] + temp < nums[i]:
                temp = nums[i]

            elif nums[i] + temp > nums[i]:
                temp = nums[i] + temp

            if max1 < temp:
                max1 = temp

        return max1


s = [-2,1,-3,4,-1,2,1,-5,4]

a = Solution()
qq = a.maxSubArray(s)
print(qq)