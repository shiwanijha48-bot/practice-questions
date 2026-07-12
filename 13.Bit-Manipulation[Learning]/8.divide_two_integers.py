#  leetcode question
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max = 2**31 - 1
        int_min = -2**31
        ans = int(dividend / divisor)
        if ans > int_max:
            return int_max
        if ans < int_min:
            return int_min
        return ans
        