class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        INF = 10000 * 80 * 80 + 1
        m = len(grid)
        n = len(grid[0])
        n_grid = [[INF] * (n + 1) for _ in range(m + 1)]
        n_grid[1][1] = 0
        cost = []
        for i in range(m):
                for j in range(n):
                    cost.append((grid[i][j], i, j))
        cost.sort(reverse = True, key = lambda x: x[0])

        while True:
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    n_grid[i][j] = min(n_grid[i][j], n_grid[i - 1][j] + 
                    grid[i - 1][j - 1], n_grid[i][j - 1] + grid[i - 1][j - 1])
            if k == 0:
                break
            k -= 1

            prev = 0
            min_cost = n_grid[cost[0][1] + 1][cost[0][2] + 1]
            for i in range(1, m * n):
                if cost[i][0] != cost[prev][0]:
                    for j in range(prev, i):
                        n_grid[cost[j][1] + 1][cost[j][2] + 1] = min_cost
                    prev = i
                min_cost = min(min_cost, n_grid[cost[i][1] + 1][cost[i][2] + 1])
            for j in range(prev, m * n):
                n_grid[cost[j][1] + 1][cost[j][2] + 1] = min_cost
        
        return n_grid[m][n]
