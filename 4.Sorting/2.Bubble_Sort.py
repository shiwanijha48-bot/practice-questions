#  method - 1
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
nums = [6, 9, 88, 2, 3 , 1, 77, 43, 90]
print(bubble_sort(nums))

# method - 2
def bubble(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if is_swap == False:
            break  # return
    return nums
num = [6, 9, 88, 2, 3 , 1, 77, 43, 90]
print(bubble(num))

# TC = O(N)
#  SC = O(1)