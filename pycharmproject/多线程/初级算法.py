nums=[1,2,3,4,5]
n=0
while n<len(nums)-3:
    for i in nums:
        n=n+1
        if nums[i]<nums[i+1] and nums[i+1]<nums[i+2]:
            print (True)
