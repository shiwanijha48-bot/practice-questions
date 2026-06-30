#  Method - 1
class Solution:
    def mark_infinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            if matrix[i][col] != 0:
                matrix[i][col] = float('inf')
        for j in range(0, c):
            if matrix[row][j] != 0:
                matrix[row][j] = float('inf')
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    self.mark_infinity(matrix, i, j)
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

#  Method - 2
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        rowTrack = [0 for _ in range(0, r)] # Track which rows to zero
        colTrack = [0 for _ in range(0, c)] # track which columns to zero
        #  First pass: mark rows and columns
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    rowTrack[i] = -1
                    colTrack[j] = -1
        #  Second pass: set Zeros
        for i in range(0, r):
            for j in range(0, c):
                if rowTrack[i] == -1 or colTrack[j] == -1:
                    matrix[i][j] = 0