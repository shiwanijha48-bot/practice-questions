n = 153
num = n
l = len(str(n))  # number of digits
x = 0   # armstrong formula checking 
while num > 0:
    last_digit = num % 10
    x = x + last_digit ** l
    num = num // 10
if x == n:
    print("Armstrong")
else:
    print("Not a Armstrong")

#  153, 1634 = armstrong number
#  TC -> O(log10(n))
