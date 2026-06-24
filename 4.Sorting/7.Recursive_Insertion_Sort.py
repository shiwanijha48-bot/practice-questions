def insertion_sort(arr, n):
    if n <= 1:
        return
    insertion_sort(arr, n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last

arr = [10, 6, 3, 88, 22, 2, 8, 90]
insertion_sort(arr, len(arr))
print(arr)