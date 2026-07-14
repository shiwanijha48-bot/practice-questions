class Solution:
    def solve(self, index, subset, nums, res):
        if index >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[index])
        self.solve(index + 1, subset, nums, res)
        subset.pop()
        self.solve(index + 1, subset, nums, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(0, [], nums, result)
        return result
    
    #  tc = o(n* 2^n). sc = o(n)