# convert int iinto binary
def convert2binary(num):
    res = ""
    while num > 0:
        if num % 2 == 1:
            res += "1"
        else:
            res += "0"
        num = num // 2
    res = res[::-1]
    return res
#  tc = o(log2n), sc = o(log2n)
print(convert2binary(13))

#  convert bin to decimal
def convert2decimal(x):
    decimal_number = 0
    power = 0
    index = len(x) - 1
    while index >= 0:
        num = int(x[index]) * (2**power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number
#  tc o(len), sc = o(!)
print(convert2decimal("1101"))

#  and = & = all true : true. all false : false
#  or = | = one true: true. one false : false
#  xor = ^ = number of 1s is odd : 1, even: 0
#  shift : right or left
''' right shift
x = 13 >> 1
1101 = 110 : right shift = 6
x = 13 >> 2
1101 = 11 : right shift = 3
x = 13 >> 4
1101 = 0 
formula : if x >> k =====  x/2**k
left shift
x = 13 << 1
1101 = 11010: 26
'''
# not = ~ = flip and check -ve if -ve: 2s complemneeh, no, then stop
