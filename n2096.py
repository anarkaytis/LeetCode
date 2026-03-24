class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m = len(grid)
        n = len(grid[0])
        result = [[0] * n for _ in range(m)]

        suffix = [0] * (m * n)
        soFar = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suffix[i * n + j] = soFar
                soFar = (soFar * grid[i][j]) % MOD
        
        soFar = 1
        for i in range(m):
            for j in range(n):
                result[i][j] = (soFar * suffix[i * n + j]) % MOD
                soFar = (soFar * grid[i][j]) % MOD
        
        return result
