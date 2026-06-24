def bubble_sort(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble_sort(arr, n-1)

arr = [10, 6, 3, 88, 22, 2, 8, 90]
bubble_sort(arr, len(arr))
print(arr)