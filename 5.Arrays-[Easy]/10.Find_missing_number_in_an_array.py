num1 = [1, 0, 3, 4]
num2 = [ 9, 6, 4, 2, 3, 5, 7, 0, 1]

#  Method - 1
def missingnum(arr):
    n = len(arr)
    return ((n+1)*n)//2 - sum(arr)
#  tc = o(n) , sc = o (1)
print(missingnum(num1))
print(missingnum(num2))

#  Metod - 2
def missing(arr):
    n = len(arr)
    for i in range(0, n+1):
        if i not in arr:
            return i

print(missing(num2))
#  tc = o(n**2), sc = o(1)

#  Method - 3

freq = {}
def missnum(arr):
    n = len(arr)
    for i in range(0, n+1):
        freq[i] = 0
    for i in arr:
        freq[i] = 1
    for k, v in freq.items():
        if v == 0:
            return k
print(missnum(num1))
print(missnum(num2))
#  tc = o(3n), sc = o(n)