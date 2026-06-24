#  Method - 1 [Head]
def func(i, N):
    if i > N:
        return
    func(i+1, N)
    print(i)
func(1,5)

# Method 2 - [Tail (backtracking)]
def func(N):
    if N == 0:
        return
    print(N)
    func(N-1)
func(5)
