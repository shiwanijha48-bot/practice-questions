class Solution:
    def isSafe1(self, row, col, board, n):
        duprow = row
        dupcol = col
        # Check upper-left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        # Reset and check left row
        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        # Reset and check lower-left diagonal
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True

    def solve(self, col, board, ans, n):
        # Base case: placed queens in all columns
        if col == n:
            ans.append(list(board))  # Make a copy of current board state
            return
        # Try placing queen in each row of current column
        for row in range(n):
            if self.isSafe1(row, col, board, n):
                # Place queen: replace '.' with 'Q' at position (row, col)
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                # Recursively solve for next column
                self.solve(col + 1, board, ans, n)
                # Backtrack: remove queen by replacing 'Q' with '.'
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def solveNQueens(self, n: int):
        ans = []
        board = ["." * n for _ in range(n)]  # Initialize n×n board with dots
        self.solve(0, board, ans, n)  # Start from column 0
        return ans

#  method - 2
class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        # Base case: placed all queens successfully
        if col == n:
            ans.append(board[:])  # Make a copy of current board
            return
        # Try each row in current column
        for row in range(n):
            # O(1) safety check using our tracking arrays
            if (
                leftrow[row] == 0
                and lowerDiagonal[row + col] == 0
                and upperDiagonal[n - 1 + col - row] == 0
            ):
                # Place queen and update all tracking arrays
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                leftrow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                # Recurse to next column
                self.solve(
                    col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n
                )
                # Backtrack: remove queen and reset tracking arrays
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n: int):
        ans = []
        board = ["." * n for _ in range(n)]
        # Initialize tracking arrays
        leftrow = [0] * n  # Track occupied rows
        upperDiagonal = [0] * (2 * n - 1)  # Track upper diagonals
        lowerDiagonal = [0] * (2 * n - 1)  # Track lower diagonals
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans


    