# n = 13, i = 2
def clear(n, i):
    x = n & ~(1<<i)
    print(x)
clear(13, 2)