#  method - 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set = {}
        for i in range(0,len(nums)):
            if nums[i] in my_set:
                my_set[nums[i]]+=1
            else:
                my_set[nums[i]]=1
        for i in range(0,len(nums)):
            if my_set[nums[i]] == 1:
                return nums[i]

#  method - 2
def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0)+ 1
        for key in hash_map:
            if hash_map[key] == 1:
                return key

        #  tc = o(n), sc = o(n/2 + 1)

#  method - 3
def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = num ^ ans
        return ans
        #  tc = o(n), sc = o(1)