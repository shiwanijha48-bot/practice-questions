def func(i):
    if i < 1:
        return 
    func(i-1)
    print("Hello")
func(5)