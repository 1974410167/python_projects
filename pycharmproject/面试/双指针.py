import math


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)

        max1 = -math.inf

        while left != right:

            min_t = min(height[left], height[right - 1])
            temp = (right - left-1) * min_t
            if temp > max1:
                max1 = temp

            if min_t == height[left]:
                left += 1
            else:
                right -= 1

        return max1
q = [1,8,6,2,5,4,8,3,7]
s = Solution()
a = s.maxArea(q)
print(a)