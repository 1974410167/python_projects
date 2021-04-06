
class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=1:
            return n
        list1 = [0 for i in range(n+1)]
        list1[0] = 0
        list1[1] = 1
        # list1[2] = 2

        for i in range(2,n+1):
            list1[i] = list1[i-1]+list1[i-2]


        return list1[n]

a =Solution()
s =a.climbStairs(81)
print(s)