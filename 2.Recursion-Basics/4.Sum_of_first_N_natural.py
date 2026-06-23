def total(num):
    if num == 1:
        return 1
    return num**3 + total(num-1)
print(total(3))
