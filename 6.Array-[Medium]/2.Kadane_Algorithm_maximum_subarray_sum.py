nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

#  Method - 1
def maxsubarray(arr):
    n = len(arr)
    maxi = float('-inf')
    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            maxi = max(maxi, total)
    return maxi
print(maxsubarray(nums))
#  TC = O(N**2), SC = O(1)


#  Method - 2 [Kadane's Algorigth]
def MaxSubArray(arr):
    n = len(arr)
    maxi = float('-inf')
    total = 0
    for i in range(0, n):
        total += arr[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
    return maxi
print(MaxSubArray(nums))
# TC = O(N), SC = O(1)
