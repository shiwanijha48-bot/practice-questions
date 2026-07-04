nums = [10, 11, 11, 12, 13, 13, 13, 13, 1, 2, 3, 4]
target = 11
target1 = 3
target2 = 8

#  Method - 1
def solve(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return True
    else:
        return False
#  TC = O(N), SC = O(1)
print(solve(nums, target))

#  Method - 2
nums1 = [8, 8, 8, 8, 8, 8, 1, 2, 3, 4, 5, 6, 8, 8]
def Solve(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] == target:
            return True
        if nums[l] == nums[mid] == nums[r]:
            l += 1
            r -= 1
            continue
        if nums[mid] <= nums[r]:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if nums[l] <= target <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return False
print(Solve(nums1, target1))

#  TC = O(log n) , SC = O(1)
#  TC = O(N/2) = O(N) : WORST CASE