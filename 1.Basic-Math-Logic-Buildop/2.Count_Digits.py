#  method 1
n = 87676672
num = n
count = 0
while num > 0:
    last_digit = num % 10
    count += 1
    num = num // 10
print(count)

# method 2
from math import *
def countdigits(n):
    print(int(log10(n)+1)) 
n = 7568768
countdigits(n)


# TC -> O(log 10(n))