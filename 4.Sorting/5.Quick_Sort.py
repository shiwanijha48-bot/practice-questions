#  Quick Sort

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while i <= high - 1 and nums[i] <= pivot:
            i += 1
        while j >= low + 1 and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index +1, high)

nums = [10, 6, 3, 88, 22, 2, 8, 90]
n = len(nums)
quick_sort(nums, 0, n - 1)
print(nums)