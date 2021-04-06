class Solution:
    def firstUniqChar(self, s: str) -> int:

        l = len(s)
        a = dict()

        for i in range(l):
            if s[i] in a:
                del a[s[i]]
            else:
                a[s[i]] = i
        return a.values()

q= Solution()
aa = q.firstUniqChar("loveleetcode")

s = list(aa)
print(type(s))
print(s[0])