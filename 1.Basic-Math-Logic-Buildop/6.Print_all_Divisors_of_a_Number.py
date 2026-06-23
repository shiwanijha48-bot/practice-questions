#  Method - 1
divisors = []
n = 10
for i in range(1, n+1):
    if n % i == 0:
        divisors.append(i)
print(divisors)
# TC = O(N), SC = O(k) k:would be the total number of factors


# Method - 2
divisors = []
n = 10
for i in range(1, n // 2 + 1):
    if n % i == 0:
        divisors.append(i)
divisors.append(n)
print(divisors)
# TC = O(N/2), SC = O(k) 

#  Method - 3
# from math import *
divisors = []
n = 10
# for i in range(1, int(sqrt(n)) + 1):
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if n // i != i:
            divisors.append(n//i)
print(divisors)

