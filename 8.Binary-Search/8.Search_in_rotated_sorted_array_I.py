nums = [1, 4, 5, 6, 8, 9, 10, 11, 15, 20]
nums1 = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
target = 15
target1 = 9
target2 = 13

#  Method - 1  [brute-force]
def solve(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    else:
        return -1
#  TC = O(N), SC = O(1)
print(solve(nums, target))
# print(solve(nums, target1))
# print(solve(nums, target2))
# print(solve(nums1, target))
# print(solve(nums1, target1))
# print(solve(nums1, target2))


#  Method - 2
def Solve(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
print(Solve(nums, target2))

#  TC = O(log n) , SC = O(1)


#  Method - 3 [Code and debug vala]
def search(nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
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
        return -1