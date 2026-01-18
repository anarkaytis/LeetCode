class Solution:
    def is_magic(self, i: int, j: int, k:int, rows: List[List[int]], cols: List[List[int]], grid: List[List[int]]) -> bool:
        sum = rows[i][j + k] - rows[i][j]
        for l in range(k):
            if rows[i + l][j + k] - rows[i + l][j] != sum:
                return False 
            if cols[i + k][j + l] - cols[i][j + l] != sum:
                return False
        diag = 0
        for l in range(k):
            diag += grid[i + l][j + l]
        if diag != sum:
            return False  
        diag = 0
        for l in range(k):
            diag += grid[i + k - 1 - l][j + l]
        if diag != sum:
            return False  
        return True

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid) + 1
        n = len(grid[0]) + 1
        rows = [[0] * n for _ in range (m)] 
        cols = [[0] * n for _ in range (m)] 
        for i in range(m - 1):
            rows[i][0] = 0
            for j in range (1, n):
                rows[i][j] = rows[i][j - 1] + grid[i][j - 1]
        for j in range(n - 1):
            cols[0][j] = 0
            for i in range (1, m):
                cols[i][j] = cols[i - 1][j] + grid[i - 1][j]
        for k in range(min(m,n), 1, -1):
            for i in range(m - k):
                for j in range(n - k):
                    if self.is_magic(i, j, k, rows, cols, grid):
                        return k
        return 1
