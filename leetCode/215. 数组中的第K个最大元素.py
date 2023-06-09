


class Solution:
    def findKthLargest(self,num, target):
        l = len(num)
        if l == 1:
            return num[0]

        left = []
        right = []
        mid = num[0]
        num = num[1:]
        for i in num:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        if len(right) >= target:
            return self.findKthLargest(right, target)
        else:
            return self.findKthLargest(left + [mid], target - len(right))


q = Solution()
c = q.findKthLargest([-1,2,0], 2)
print(c)