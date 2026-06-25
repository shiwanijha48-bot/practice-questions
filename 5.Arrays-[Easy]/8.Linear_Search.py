nums = [2, 3, 5, 89 ,6]
x = 6
for i in range(0, len(nums)):
    if nums[i] == x:
        print(i)
    print("-1")


def linearSearch(n, num, arr):
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
    return -1
print(linearSearch(5, 5, nums))
#  tc = o(n)
#  sc = o(1)