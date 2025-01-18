class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        avaliable_move = set()
        avaliable_move.add((0,0))
        visited = [[False] * n for _ in range (m)]
        visited[0][0] = True

        directions = {
            1 : (0,1),
            2 : (0, -1),
            3 : (1, 0),
            4 : (-1, 0),
        }

        for cost in range(m + n):
            intermidiate = set()
            for (x, y) in avaliable_move:
                while True:
                    (dx, dy) = directions[grid[x][y]]
                    x += dx
                    y += dy
                    if (x < 0) or (y < 0) or (x >= m) or (y >= n) or visited[x][y]:
                        break
                    visited[x][y] = True
                    intermidiate.add((x, y))

            avaliable_move |= intermidiate
            if (m - 1, n - 1) in avaliable_move:
                return cost
            intermidiate.clear()
            for (x, y) in avaliable_move:
                for (dx, dy) in directions.values():
                    x1 = x + dx
                    y1 = y + dy
                    if (x1 < m) and (y1 < n) and (x1 >= 0) and (y1 >= 0) and not visited[x1][y1]:
                        visited[x1][y1] = True
                        intermidiate.add((x1, y1)) 
            avaliable_move = intermidiate
