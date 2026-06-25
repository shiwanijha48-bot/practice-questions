arr = [3, 6, 8, 30, 1, 99]

#  method -1
n = len(arr)
maxi = float('-inf')
for i in range(n-1):
    maxi = max(maxi, arr[i+1])

print(maxi)

#  method -2
maxim = arr[0]
for i in range(1, n):
    if arr[i] > maxim:
        maxim = arr[i]
print(maxim)

#  method - 3
maxim = float('-inf')
for i in range(1, n):
    if arr[i] > maxim:
        maxim = arr[i]
print(maxim)

#  TC = O(N)
#  SC = O(1)