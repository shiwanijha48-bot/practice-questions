def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print(count_set_bits(13))
print(count_set_bits(4))

#  method - 2
def Count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
print(Count_set_bits(13))
print(Count_set_bits(4))