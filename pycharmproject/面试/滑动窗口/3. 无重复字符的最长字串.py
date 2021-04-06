import math
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0


        list1 = list()
        l = len(s)
        i , j =0 ,0

        max_1 = -math.inf
        while j<= l - 1:


            if len(s[i:j + 1]) == len(set(s[i:j + 1])):
                if max_1 <= j - i + 1:
                    max_1 = j - i + 1

            while len(s[i:j + 1]) != len(set(s[i:j + 1])) and i <= j:
                i += 1

            j += 1

        return max_1

s =  "abcabcbb"
a = Solution()
ss = a.lengthOfLongestSubstring(s)
print(ss)