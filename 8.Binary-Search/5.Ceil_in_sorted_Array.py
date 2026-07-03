#  Floor  = largest number in array <= target
#  Ceil  = smallest number in array >= target

nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]

def func(nums, target):
    n = len(nums)
    floor = -1
    ceil = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    print([floor, ceil])
func(nums, 6)

#  TC = O(log n)