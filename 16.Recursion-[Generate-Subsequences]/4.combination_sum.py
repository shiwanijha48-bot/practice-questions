nums = [2, 3, 6, 7]
target = 7

def solve(self, index, total, subset, nums, target, result):
    if total == target:
        result.append(subset.copy())
        return
    elif total > target:
        return
    if index >= len(nums):
        return
    sum = total + nums[index]
    subset.append(nums[index])
    self.solve(index, sum, subset, nums, target, result)
    sum = total 
    subset.pop()
    self.solve(index + 1, sum, subset, nums, target, result)
def combinationsum(self, candidates, target):
    res = []
    self.solve(0, 0, [], candidates, target, res)
    return res

#  tc = o(2^t * k) 
#  sc = o(t) + o(k)
# t = no of times picked an element