nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 20
# 1) Binary search
def search(nums, target): 
    n = len(nums)
    low, high = 0, n - 1
    ans = n                     # default insert position = end
    while low <= high:
        mid = (low + high) // 2  # midpoint of the window
        if nums[mid] >= target:
            ans = mid            # nums[mid] is a valid (or exact) position
            high = mid - 1       # keep searching left half
        else:                    # nums[mid] < target
            low = mid + 1        # search right half
    return ans                   # final insertion index
print(search(nums, target))
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