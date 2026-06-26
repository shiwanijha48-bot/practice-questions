nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13
#  Method - 1
def twosum(arr, target):
        res = []
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == target:
                    res.append(i)
                    res.append(j)
        return res
print(twosum(nums, target))
# TC = O(N**2), SC = O(1)


# Meethod - 2
def TwoSum(arr, target):
    n = len(arr)
    hash_map = {}
    for i in range(0, n):
        rem = target - arr[i]
        if rem in hash_map:
            return [hash_map[rem], i]
        hash_map[arr[i]] = i
print(TwoSum(nums, target))
#  TC = O(N), SC = O(1)