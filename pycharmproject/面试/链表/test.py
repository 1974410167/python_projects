s = [2,2,1,1,1,2,2]
class Solution:
    def majorityElement(self, nums):
        hash1 = {}
        max1 = 0
        sign = 0
        for i in nums:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1

            if max1 < hash1[i]:
                max1 = hash1[i]
                sign = i
        return sign

a = Solution()
q = a.majorityElement(s)
print(q)


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        l1 = len(matrix)
        l2 = len(matrix[0])

        i=0

        j=0

        while i<l2-1 and j<l1-1:

            if matrix[j][i] == target:
                return True
            elif matrix[j][i] < target:
                i -= 1


