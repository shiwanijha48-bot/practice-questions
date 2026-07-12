def toggle(n, i):
    x = n ^ (1 << i)
    print(x)
toggle(13, 2)
toggle(13, 1)