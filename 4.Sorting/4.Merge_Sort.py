#  merge sort
def merge_array(left, right):
    res = []
    i , j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < n:
        res.append(left[i])
        i += 1
    while j < m:
        res.append(right[j])
        j += 1
    return res
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_half = merge_sort(left_arr)
    right_half = merge_sort(right_arr)
    return merge_array(left_half, right_half)

arr = [10, 6, 3, 88, 22, 2, 8, 90]
print(merge_sort(arr))

#  TC = O(n log n)
#  SC = O(n); extra arrays used in merging