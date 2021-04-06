class Solution():
    def HalfSearch(self,OrderedList, key):
        left=0
        right = len(OrderedList)
        while left <= right:
            mid = (left + right) //2
            if key == OrderedList[mid]:
                return mid
            elif key > OrderedList[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return None
A=Solution()
a=A.HalfSearch([1,2,3,4,5],5)
print (a)


