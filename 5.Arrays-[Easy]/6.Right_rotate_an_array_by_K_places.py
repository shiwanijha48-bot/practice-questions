nums = [3, 9, 5, 6, 7, 2]
k = 3

#  method - 1
n = len(nums)
rotations = k% n
for _ in range(0, rotations):
    e = nums.pop()
    nums.insert(0, e)
print(nums)
#  tc = o(r*n)
#  sc = o(1)

#  method - 2
k = n % k
nums[:] = nums[n-k:] + nums[:n-k]
print(nums)

#  tc = o(n)
#  sc = o(1)

#  methpod - 3
'''Trick: rev the last k elements, 
rev the remaining elements.. 
and then reverse the whole array'''

def rev(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r] , nums[l]
        l += 1
        r -= 1
rev(nums, n-k, n-1)  # rev the last k elemnts
rev(nums, 0, n-k-1)  # rev the remaning elemnets
rev(nums, 0, n-1)  # rev the whole array 
print(nums)

#  tc = o(n)
#  sc = o(1)