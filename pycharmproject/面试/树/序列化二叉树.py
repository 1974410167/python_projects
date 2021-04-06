class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        t = []

        for i in range(m):
            t.append([])
            for j in range(n):
                t[i].append(1)
        # return t
        for q in range(m):
            for p in range(n):
                if q!=0 and p!=0:
                    t[q][p] = max(t[q-1][p],t[q][p-1])+1

        return t[-1][-1]

s = Solution()
a = s.uniquePaths(3,7)
print(a)