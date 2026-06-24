#  1 to N
#  Method - 1 [TAIL]
def func(i, N):
    if i > N:
        return
    print(i)
    func(i+1, N)
func(1,4)

#  TC = O(N)
#  SC = O(N)

# Method - 2 [HEAD]
def func(n):
    if n == 0:
        return
    func(n-1)
    print(n)
func(5)