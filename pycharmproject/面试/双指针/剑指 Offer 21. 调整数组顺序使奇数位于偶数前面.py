"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


"""
class Solution:
    def exchange(self, nums):
        l = 0
        r = len(nums )-1
        if r== 1:
            return nums
        sign = set()

        while l < r:

            if nums[l] % 2 == 0:
                if 'l' not in sign:
                    sign.add('l')
            else:
                l += 1

            if nums[r] % 2 == 1:
                if 'r' not in sign:
                    sign.add('r')
            else:
                r -= 1

            if len(sign) == 2:
                nums[l], nums[r] = nums[r], nums[l]
                sign.clear()
                l += 1
                r -= 1

        return nums
nums =  [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]

s = Solution()
a = s.exchange(nums)
print(a)