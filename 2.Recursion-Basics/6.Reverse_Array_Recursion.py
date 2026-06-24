#   Reverse Array Recursion

#  Method - 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def func(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)

func(nums ,2 , 5)
print(nums)

#  Method - 2 [using while loop]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
def rev(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r] , arr[l]
        l += 1
        r -= 1
rev(arr, 2, 5)
print(arr)