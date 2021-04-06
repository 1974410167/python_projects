class Solution:
    def combinationSum(self, candidates, target):

        def dfs(path,target):

            if target < 0:
                return

            if target == 0:
                res.append(path)
                return

            for index in range(size):

                dfs(path + [candidates[index]],target -candidates[index])


        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(path,target)
        return res

ss = [2,3,6,7]
a = 7

S = Solution()
aa = S.combinationSum(ss,a)
print(aa)
