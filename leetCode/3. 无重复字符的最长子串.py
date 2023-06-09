


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        left = 0
        right = 1
        res = 1
        while right < l:
            cur = s[left:right+1]
            cur_length = len(cur)
            if self.is_valid_str(cur):
                if cur_length > res:
                    res = cur_length
                right += 1
            else:
                left += 1
        return res

    def is_valid_str(self, m: str) -> bool:
        d = set()
        for i in m:
            if i in d:
                return False
            d.add(i)
        return True

q = Solution()
r = q.lengthOfLongestSubstring("pwwkew")
print(r)