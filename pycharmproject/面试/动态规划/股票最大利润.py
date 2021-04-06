import math
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        t1 = math.inf
        L = len(prices)

        t_nums = [0 for i in range(L)]

        for i in range(L):
            if prices[i] < t1:
                t1 = prices[i]
                t_nums[i] = t1

            elif prices[i] >= t1:
                t_nums[i] = t1

        re = 0
        for j in range(L):
            if prices[j] > t_nums[j]:
                q = prices[j] - t_nums[j]
                if q > re:
                    re = q

        return re
qq = [3,3]
s = Solution()
q = s.maxProfit(qq)
print(q)