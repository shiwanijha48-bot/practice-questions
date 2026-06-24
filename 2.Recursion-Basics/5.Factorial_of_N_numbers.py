#  Factorial 

def fact(n):
    if n <= 1:
        return 1
    return fact(n-1)*n
print(fact(5))

# TC = O(n)
#  SC = O(n) stack space