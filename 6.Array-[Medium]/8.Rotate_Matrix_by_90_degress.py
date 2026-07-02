matrix = [[1, 2, 3, 4], [5 ,6 , 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


# Method - 1 [ extra res matrix le ke roate it]
def rotate(matrix):
    r = len(matrix)
    c = len(matrix[0])
    n = len(matrix)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(r):
        for j in range(c):
            res[j][(n-1)-i] = matrix[i][j]
    return res
# print(rotate(matrix))
#  TC = O(N**2)
#  SC = O(N**2)

#  Method - 2 [transpose karke, reverse it]
def rotata_matrix(matrix):
    n = len(matrix)
    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix

print(rotata_matrix(matrix))
#  TC = O(N**2), SC = O(1)