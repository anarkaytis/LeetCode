class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        
        if total & 1 != 0:
            return False
        
        soFar = 0
        total //= 2
        for row in rows:
            soFar += row
            if soFar == total:
                return True
            if soFar > total:
                break
        
        soFar = 0
        for col in cols:
            soFar += col
            if soFar == total:
                return True
            if soFar > total:
                break
        return False
