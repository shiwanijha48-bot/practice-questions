def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        mini_index = i
        for j in range(i+1, n):
            if nums[j] < nums[mini_index]:
                mini_index = j
        nums[i], nums[mini_index] = nums[mini_index], nums[i]
    return nums
nums = [10,6,3,88,22,2, 8, 90]
print(selection_sort(nums))