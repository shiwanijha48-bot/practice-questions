arr = [2, 5, 7, 9, 33, 55, 77, 43, 89, 12]
arr1 = [2, 5, 7, 9, 33, 55, 77, 43, 89, 12]
#  Method - 1
arr1.sort()
print(arr1[-2])

#  Method - 2
f = float('-inf')
s = float('-inf')
n = len(arr)
for i in range(0, n-1):
    if arr[i] > f:
        s = f
        f = arr[i]
    elif arr[i] > s and arr[i] != f:
        s = arr[i]
print(s)

#  Method - 3
arr2 = [2, 5, 7, 9, 33, 55, 77, 43, 89, 12]
f = float('-inf')
s = float('-inf')
n = len(arr2)
for i in range(0, n-1):
    f = max(f, arr2[i])
for i in range(0, n):
    if arr2[i] > s and arr2[i] != f:
        s = arr2[i]
print(s)

