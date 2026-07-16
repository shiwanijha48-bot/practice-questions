nums = [5, 1, 1, 9, 2, 10]
k = 9 # atrget
result = []
def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    sum = total + nums[index]
    pick = backtrack(index + 1, sum, subset)
    if pick == True:
        subset.pop()
    sum = total
    not_pick = backtrack(index + 1, sum, subset)
    return not_pick

#  tc   = 2^n 
# / sc  = n
