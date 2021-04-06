from typing import List
import copy

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []

        if target <= 2:
            return res


        i, j = 1, 2

        m = target // 2 + 1


        t = [i,j]
        sign = i+j

        while j <= m:


            if sign == target:

                p = copy.copy(t)
                res.append(p)

                j += 1
                sign += j
                t.append(j)

            elif sign < target:
                j += 1
                sign += j
                t.append(j)


            elif sign > target:

                sign -= i
                i += 1
                t.pop(0)

        return res
target = 9
s = Solution()
q = s.findContinuousSequence(target)
print(q)