class Solution:
    def distributeCandies(self,candies):
        t = set(candies)
        l1 = len(t)
        l2 = len(candies)
        num = []
        if l1>=l2/2:
            return int(l2/2)
        else:
            return int(l1)


s = Solution()
a = s.distributeCandies([1,1,2,3])
print(a)