n = 123421
rev = 0
num = n
while num > 0:
    last_digit = num % 10
    rev = rev * 10 +  last_digit
    num = num //10

if rev == n :
    print("Yes, Palindrome")
else:
    print("Not a Palindrome")