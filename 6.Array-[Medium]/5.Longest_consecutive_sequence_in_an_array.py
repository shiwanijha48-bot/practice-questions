nums = [1, 99, 101, 98, 2, 5, 3, 100]

#  Method - 1
def solve(arr):
    n = len(arr)
    maxi = 0
    for i in range(0, n):
        x = arr[i]
        count = 1
        while x+1 in arr:
            count += 1
            x = x+1
        maxi = max(maxi, count)
    return maxi
print(solve(nums))
#  TC = O(N**2), SC = O(1)

# Method - 2
def Solve(arr):
    arr.sort()
    n = len(arr)
    last_smaller = float('-inf')
    count = 0
    longest = 0
    for i in range(0, n):
        x = arr[i]
        if x -1 ==last_smaller:
            count += 1
            last_smaller = x
        elif x != last_smaller:
            count = 1
            last_smaller = x
        longest = max(longest, count)
    return longest
print(Solve(nums))
#  TC = O(NLOGN + N), SC = O(1)

#  Method - 3
def Func(arr):
    my_set = set(arr)
    longest = 0
    for num in my_set:
        if num-1 not in my_set:
            x = num
            count = 1
            while x +1 in my_set:
                count += 1
                x += 1
            longest = max(longest, count)
    return longest
#  TC = O(3N) = O(N),  SC = O(N)
print(Func(nums))





#  Method [doesnt works for all questions]
# def func(arr):
#     n = len(arr)
#     maxi = 0
#     count = 0
#     for i in arr:
#         if i+1  in arr:
#             count += 1
#             maxi = max(maxi, count)
#         if i-1 in arr:
#             count += 1
#             maxi = max(maxi, count)
#         else:
#             count = 0
#     return maxi
# print(func(nums))