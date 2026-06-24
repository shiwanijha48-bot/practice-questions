"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
def findFrequency( arr, x):
        # code here
        count = 0
        for i in arr:
            if i == x:
                count += 1
        return count
nums = [1,2,3,4,1,3,6,8,3,2,1]
print(findFrequency(nums, 1))