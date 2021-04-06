import math
class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''

        m = math.inf

        min_word = ''

        for i in strs:
            ll = len(i)
            if ll<m:
                min_word = i
                m = ll


        result = ''

        L1 = len(strs)

        for i in range(m):
            t = 0
            for word in strs:
                if min_word[i]==word[i]:
                    t+=1

                if t==L1:
                    result += min_word[i]

        return result
s = ["flower","flow","flight"]

a = Solution()
q = a.longestCommonPrefix(s)
print(q)