nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
# Method - 1
def conscount(arr):
    n = len(arr)
    count = 0
    ans = 0
    for i in range(0, n):
        if arr[i] == 1:
            count += 1
            ans = max(count, ans)
        else:
            count = 0
    return ans
print(conscount(nums))

# Method - 2
def consecutivecount(arr):
    n = len(arr)
    count = 0
    ans = 0
    for i in range(0, n):
        if arr[i] == 1:
            count += 1
        else:
            ans = max(count, ans)
            count = 0
    return max(ans, count)
print(consecutivecount(nums))

# TC = O(N+1+1) = O(N), SC = O(1)