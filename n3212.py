class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix_x = [0] * n
        prefix_y = [0] * n
        result = 0
        for i in range(m):
            soFar_x = 0
            soFar_y = 0
            for j in range(n):
                if grid[i][j] == "X":
                    prefix_x[j] += 1
                soFar_x += prefix_x[j]
                if grid[i][j] == "Y":
                    prefix_y[j] += 1
                soFar_y += prefix_y[j]
                if (soFar_x != 0) and (soFar_x == soFar_y):
                    result += 1
        return result     
