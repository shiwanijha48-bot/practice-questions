# Check if string palindrome

#  Method -1  [Recursive (functional)]
s = "abcdef"
def rev(s, i, j):
    if s[i] == s[j]:
        i += 1
        j -= 1
    else:
        return False
    return True
x = rev(s,0, len(s)-1)
print(x)
#  TC = O(n), SC = O(n); rec stack

#  Method - 2  [Reverse string build]
s2 = "niting"
rev = ""
for i in s2:
    rev = i + rev
if rev == s2:
    print(True)
else:
    print("False")
print(rev)
#  TC = O(n^2), SC = O(n); rev string

#  Method - 3  [Two pointers iterative]
s3 = "ghiihg"
n = len(s3)
l = 0
r = n - 1
def revstr(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
y  = revstr(s3, 0, n-1)
print(y)
#  TC = O(n), SC = O(1)

#  Method - 4  [Two pointers recursive]
def funct(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return funct(s, l+1, r-1)

print(funct(s3, 0, n-1))
# TC = O(n), SC = O(n): rec stack



