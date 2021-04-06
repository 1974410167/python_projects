

nums = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7],
]


a = [[1,2,3],
     [4,5,6],
     [7,8,9]]


class Solution:
    def spiralOrder(self, matrix):

        if not matrix:
            return []
        lx = len(matrix[0])
        ly = len(matrix)
        l, r, t, b = 0, lx - 1, 0, ly - 1

        res = []
        while True:

            if l > r:
                break
            for lr in range(l, r + 1):
                t1 = matrix[t][lr]
                res.append(t1)
            t += 1

            if t > b:
                break
            for tb in range(t, b + 1):
                t2 = matrix[tb][r]
                res.append(t2)
            r -= 1

            if l > r:
                break
            for rl in range(r, l - 1, -1):
                t3 = matrix[b][rl]
                res.append(t3)
            b -= 1

            if t > b:
                break
            for bt in range(b, t - 1, -1):
                t4 = matrix[bt][l]
                res.append(t4)
            l += 1
        return res

ss = Solution()
q = ss.spiralOrder(nums)
print(q)