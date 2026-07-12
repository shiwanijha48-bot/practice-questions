def power2(n):
    if n & n-1 == 0:
        return True
    else:
        return False
    
print(power2(8))
print(power2(5))
print(power2(64))