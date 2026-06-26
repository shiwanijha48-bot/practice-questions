arr= [5, 10, -3, -1, -10, 6]

#  Method -1
def func(nums):
    n = len(nums)
    pos = []
    neg = []
    res = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(0,n//2):
        res.append(pos[i])
        res.append(neg[i])
    return res
print(func(arr))
#  TC = O(N), SC = O(N)