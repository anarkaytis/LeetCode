class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        up = sum(grid[0])
        min_path = up - grid[0][0]
        down = 0
        for k in range(0, n):
            up -= grid[0][k]
            max_path = max(up, down)
            down += grid[1][k]
            min_path = min(min_path, max_path)
        return min_path
