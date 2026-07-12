# / method - 1  [left shift]
def checkKthBit(self, n, k):
        if n & (1 << k) != 0:
            return True
        return False
#  tc = o(1),  sc = o(1)


# /method - 2 [right shift]

def checkKthBit(self, n, k):
        if (n >> k) & 1 == 1:
            return True
        return False
#  tc = o(1),  sc = o(1)