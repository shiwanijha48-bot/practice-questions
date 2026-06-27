nums = [[5, 20, 3], [7, -10, 9], [1, -52, 6]]

# Method - 1 [print elements of 2d matrix]
rows = len(nums)
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        print(nums[i][j])
print("-----------------------------")


#  Method - 2
# [print upper traingle]
rows = len(nums)
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        if j >= i:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()
print("-----------------------------------------")

#  Method - 3
# [print lower traingle]
rows = len(nums)
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        if j <= i:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()
print("-----------------------------------------")

#  Method - 4
# [print diagonal]
rows = len(nums)
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        if j == i:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()
print("-----------------------------------------")

#  Method - 5
# [print 2nd  diagonal]
rows = len(nums)
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i + j == 2:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()
print("-----------------------------------------")

#  Method - 6
# [print transpose]
rows = len(nums)
cols = len(nums[0])
res = [[0]*rows for _ in range(cols)]
for i in range(0, rows):
    for j in range(0, cols):
        res[j][i] = nums[i][j]
for row in res:
    print(row)
print("-----------------------------------------")

