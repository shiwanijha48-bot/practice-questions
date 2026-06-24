#  Sum of first N natural numbers

#  Method - 1 [Functional Recursion]
def total(num):
    if num == 1:
        return 1
    return num + total(num-1)
print(total(3))

# Method - 2 [Parameterized Recursion]
def func(sum, i, n):
    if i > n:
        print(sum)
        return
    func(sum + i, i+1, n)
func(0,1,4)
