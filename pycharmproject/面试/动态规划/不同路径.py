nums = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]
for m in range(7):
    nums[0][m] = 1


for n in range(3):
    nums[n][0] = 1

print(nums)
for i in range(1,3):
    for j in range(1,7):
        nums[i][j] = nums[i][j-1]+nums[i-1][j]

print(nums)

# def ss():
#     nums = [0]*7
#
#     nums[1][0] =1
#     nums[0][1] =1
#
#     for i in range(2,7):
#         for j in range(1):
#             nums[i][j] = 1
#
#     print(nums)
#     return nums[-1][-1]

# print(ss())