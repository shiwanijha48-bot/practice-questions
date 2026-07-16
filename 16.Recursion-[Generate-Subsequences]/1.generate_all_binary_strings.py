class Solution:
    def solve(self, index,  numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        numbers[index] = "0"
        self.solve(index + 1, numbers, result)

        numbers[index] = "1"
        self.solve(index + 1, numbers, result)
            
    def binstr(self, n):
        # code here
        numbers = ["0"] * n
        result = []
        self.solve(0, numbers, result)
        return result
        

#  gfg solution
class Solution:
    def solve(self, index, flag, numbers, result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return

        numbers[index] = "0"
        self.solve(index + 1, True, numbers, result)

        if flag:
            numbers[index] = "1"      # <-- assignment, not comparison
            self.solve(index + 1, False, numbers, result)
            numbers[index] = "0"

    def binstr(self, n):
        numbers = ["0"] * n
        result = []
        self.solve(0, True, numbers, result)
        return result