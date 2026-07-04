nums = [4, 5, 6, 7, 1, 2]

#  Method - 1
def solve(nums):
    n = len(nums)
    mini = float('inf')
    for i in range(n):
        mini = min(mini, nums[i])
    return mini
print(solve(nums))

#  Method - 2
def Solve(nums):
    n = len(nums)
    mini = float('inf')
    l = 0
    h = n -1 
    while l <= h:
        mid = (l + h)//2
        if nums[mid] <= nums[h]:
            mini = min(mini, nums[mid])
            h = mid - 1
        else:
            mini = min(mini, nums[l])
            l = mid + 1
    return mini
print(Solve(nums))

