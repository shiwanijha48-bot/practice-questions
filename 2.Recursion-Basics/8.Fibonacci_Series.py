#  Fibonnacci series

#  Method - 1
def func(n):
    if n == 0 or n == 1:
        return n
    return func(n-1) + func(n-2)

print(func(8))

#  TC = O(2^n), SC = O(n)
