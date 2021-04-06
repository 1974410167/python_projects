from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:

        restlt = []
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]

        def help(k, res):

            if k == 0:
                restlt.append(res)
                return
            for i in [shorter, longer]:
                res += i
                help(k - 1, res)

        res = 0
        help(k, res)

        return restlt
shorter = 1
longer = 2
k = 3
s = Solution()
a = s.divingBoard(shorter,longer,k)
print(a)