

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        if len(s)==1:
            return 1

        L = len(s)

        max1 = 0
        for i in range(L-1):
            t = s[i]
            for j in range(i+1,L):
                if len(t) == len(set(t)) and len(t)>max1:
                    max1=len(t)

                t += s[j]


        return max1

s = "pwwkew"

# a = len(s)
#
# print(a)

a = Solution()
q = a.lengthOfLongestSubstring(s)

print(q)