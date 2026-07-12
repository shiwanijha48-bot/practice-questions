#  remove the last set bit [right most]
#  n = 16 : 100000 : 000000,   n = 12 : 1100 : 1000  
def func(n):
    return n | (n + 1)


print(func(10))