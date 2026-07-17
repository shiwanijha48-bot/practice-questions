target = 7

class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        if target == 0:
            result.add(tuple(subset.copy()))
            return
        elif target < 0:
            return
        if index >= len(candidates):
            return
        subset.append(candidates[index])
        target -= candidates[index]
        self.backtrack(subset, index+1, target, result, candidates)
        subset.pop()
        target += candidates[index]
        self.backtrack(subset, index + 1, target, result, candidates)
            
    def combinationSum2(self, candidates):
        candidates.sort()
        result = set()
        self.backtrack([], 0, target,  result, candidates)
        return list(result)
    


#  method - 2
class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        if target == 0:
            result.append(subset.copy()) 
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            subset.pop()

    def combinationSum2(self, candidates):
        candidates.sort()  # Sort to enable duplicate skipping and early termination
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result
    
    