class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = [0] * n
        result = 0
        for i in range(m):
            soFar = 0
            for j in range(n):
                prefix[j] += grid[i][j]
                soFar += prefix[j]
                if soFar > k:
                    break
                result += 1
            if prefix[0] > k:
                break
        return result  
