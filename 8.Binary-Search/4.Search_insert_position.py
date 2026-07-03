nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 20
# 1) Binary search
def search(nums, target): 
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            ub = mid 
            high = mid - 1
        else:
            low = mid + 1
    print(ub)
search(nums, target)
#  TC = O(log n)

# 2) Linear search
def solve(nums, target):
    # Scan each element once
        for i in range(len(nums)):
            if nums[i] >= target:      # found position or exact match
                return i
        return len(nums)               # insert after the last element

print(solve(nums, target))
#  TC = O(N)