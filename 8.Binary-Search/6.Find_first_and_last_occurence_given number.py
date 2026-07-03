nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 3 # [2,6]

#  Method - 1

def solve(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
print(solve(nums, target))

#  Method - 2
def lowerbound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            lb = mid 
            high = mid - 1
        else:
            low = mid + 1
    return lb
# lowerbound(arr, 7)

def upperbound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] > target:
            ub = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ub
# upperbound(arr,3)
lb = lowerbound(nums, target)
if lb == -1:
    print([-1, -1])
ub =  upperbound(nums, target)
print([lb, ub - 1])

#  Tc = o(logn)
