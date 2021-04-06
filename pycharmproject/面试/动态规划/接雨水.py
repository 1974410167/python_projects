


class Solution:
    def trap(self, height) -> int:
        L = len(height)

        max_left = [0 for _ in range(L)]

        for i in range(1, L):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        max_right = [0 for _ in range(L)]

        for j in range(L - 2, 0, -1):
            max_right[j] = max(max_right[j + 1], height[j + 1])

        num = 0
        for k in range(1, L - 1):
            min_1 = min(max_left[k], max_right[k])

            if min_1 > height[k]:
                num = num + min_1 - height[k]

        return num

s = [0,1,0,2,1,0,1,3,2,1,2,1]

q = Solution()
a = q.trap(s)
print(a)