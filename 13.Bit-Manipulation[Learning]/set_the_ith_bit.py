def func(n, i):
    #  n = 9 and i = 2
    x = n | (1<<i)
    print(x)

func(9,2)
func(13,2)

#  tc = o(1), sc = o(1)