#  Method - 1
divisors = []
n = 7
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if n // i != i:
            divisors.append(n//i)
if len(divisors) > 2:
    print("Not a Prime Number")
else:
    print("Prime Number")

#  Method - 2
def isprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(isprime(13))

# Method - 3
def isprime(n):
    if n == 1:
        return False
    for i in range(2, n// 2 + 1):
        if n % i == 0:
            return False
    return True
print(isprime(13))

#  Method - 4
def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(isprime(13))
        