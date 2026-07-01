matrix = [[7, 9, 2, 3], [20, 8, 0, 10], [29, 0, -10, 5] , [4, 14, 6, 7]]

#  Method - 1

def mark(matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            if matrix[i][col] != 0:
                matrix[i][col] = "#"
        for j in range(0, c):
            if matrix[row][j] != 0:
                matrix[row][j] = '#'
        
def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    mark(matrix, i, j)
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
        return matrix

#  Method - 2
def SetZeroes(matrix):
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
        return matrix

print(setZeroes(matrix))
# print(SetZeroes(matrix))