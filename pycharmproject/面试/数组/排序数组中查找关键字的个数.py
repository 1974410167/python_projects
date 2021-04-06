s = [1,1,2]

list
class Solution:
    def search(self, nums, target):

        L = len(nums)
        result = 0
        while nums:
            l = len(nums)
            mid = l // 2
            if nums[mid] > target:
                nums = nums[:mid]
            elif nums[mid] < target:
                nums = nums[mid + 1:]
            else:
                result += 1
                break
        index = nums.index(target)
        if result!=0:
            t = index
            while True:
                t += 1
                if t == L:
                    break
                if nums[t] == target:
                    result += 1
                else:
                    break
            t1 = index
            while True:
                t1 -= 1
                if t1 < 0:
                    break
                if nums[t1] == target:
                    result += 1
                else:
                    break
        return result


a = Solution()
q = a.search(s,2)
print(q)