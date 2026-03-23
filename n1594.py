class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 1000000000 + 7
        m = len(grid)
        n = len(grid[0])
        minPath = [[0] * n for _ in range(m)]
        maxPath = [[0] * n for _ in range(m)]
        minPath[0][0] = grid[0][0]
        maxPath[0][0] = grid[0][0]

        for i in range(1, m):
            minPath[i][0] = minPath[i - 1][0] * grid[i][0]
            maxPath[i][0] = maxPath[i - 1][0] * grid[i][0]
        for j in range(1, n):
            minPath[0][j] = minPath[0][j - 1] * grid[0][j]
            maxPath[0][j] = maxPath[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    maxPath[i][j] = max(maxPath[i - 1][j], maxPath[i][j - 1]) * grid[i][j]
                    minPath[i][j] = min(minPath[i - 1][j], minPath[i][j - 1]) * grid[i][j]
                if grid[i][j] < 0:
                    maxPath[i][j] = min(minPath[i - 1][j], minPath[i][j - 1]) * grid[i][j]
                    minPath[i][j] = max(maxPath[i - 1][j], maxPath[i][j - 1]) * grid[i][j]

        return (maxPath[m - 1][n - 1]) % MOD if maxPath[m - 1][n - 1] >= 0 else -1 
