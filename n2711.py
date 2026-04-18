class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0] * n for _ in range(m)]
        for j in range(n):
            diag = []
            x = 0
            y = j
            while (x < m) and (y < n):
                diag.append(grid[x][y])
                x += 1
                y += 1
            x = 0
            y = j
            while (x < m) and (y < n):
                result[x][y] = abs(len(set(diag[: x])) - len(set(diag[(x + 1): ])))
                x += 1
                y += 1
        for i in range(1, m):
            diag = []
            x = i
            y = 0
            while (x < m) and (y < n):
                diag.append(grid[x][y])
                x += 1
                y += 1
            x = i
            y = 0
            while (x < m) and (y < n):
                result[x][y] = abs(len(set(diag[: y])) - len(set(diag[(y + 1): ])))
                x += 1
                y += 1
        return result
