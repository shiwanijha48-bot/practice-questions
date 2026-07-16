nums = [5, 1, 1, 9, 2, 10]
k = 1
result = []
def backtrack(index, total):
    if total == k:
        return 1
    elif total > k:
        return 0
    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = backtrack(index + 1, sum)
    sum = total
    not_pick = backtrack(index + 1, sum)
    return not_pick + pick
print(backtrack(0,0))
#  tc   = 2^n 
# / sc  = n
