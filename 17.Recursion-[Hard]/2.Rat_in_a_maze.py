
class Solution:
    def solve(self, i, j, maze, n, ans, move, vis, di, dj):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        dir = "DLRU"
        for ind in range(4):
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if (0 <= nexti < n and
                0 <= nextj < n and
                not vis[nexti][nextj] and
                maze[nexti][nextj] == 1):
                vis[i][j] = 1
                self.solve(nexti, nextj, maze, n, ans, move + dir[ind], vis, di, dj)
                vis[i][j] = 0

    def ratInMaze(self, maze):
        n = len(maze)
        ans = []
        if maze[0][0] == 0:
            return ans
        vis = [[0] * n for _ in range(n)]
        # Down, Left, Right, Up
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        self.solve(0, 0, maze, n, ans, "", vis, di, dj)
        return ans

    #  Geeks for geeks question