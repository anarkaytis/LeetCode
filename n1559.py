class Solution:
    def dfs(self, x0: int, y0: int, x1: int, y1: int) -> bool:
        if self.visited[x0][y0]:
            return True
        self.visited[x0][y0] = True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1,0)]:
            x2 = x0 + dx
            y2 = y0 + dy
            #print("letter: " + self.grid[x0][y0] + " x2 : " + str(x2) + " y2 : " + str(y2))
            if (x2 < 0) or (x2 >= self.m) or (y2 < 0) or (y2 >= self.n) or (self.grid[x2][y2] != self.grid[x0][y0]) or ((x2 == x1) and (y2 == y1)):
                continue
            if self.dfs(x2, y2, x0, y0):
                return True
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        for x in range(self.m):
            for y in range(self.n):
                if not self.visited[x][y]:
                    if self.dfs(x, y, -1, -1):
                        return True
        return False
