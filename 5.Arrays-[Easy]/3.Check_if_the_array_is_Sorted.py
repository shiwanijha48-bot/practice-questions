arr = [1, 6, 3, 99, 88,56, 2,5, 34, 56]

def checksort(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(checksort(arr))
arr1 = [1, 2, 3,4,5]
print(checksort(arr1))

