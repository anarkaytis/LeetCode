class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = {}
        dp[(0,0)] = {k : 0}

        for x in range(m):
            for y in range(n):
                if (x == 0) and (y == 0):
                    continue
                top = dp.get((x - 1, y), {})
                left = dp.get((x, y - 1), {})
                curr = {}
                for key in (top.keys() | left.keys()):
                    if grid[x][y] == 0:
                        curr[key] = max(top.get(key, 0), left.get(key, 0))
                    elif key >= 1:
                        curr[key - 1] = max(top.get(key, 0), left.get(key, 0)) + grid[x][y]
                dp[(x, y)] = curr
        return max(dp[(m - 1, n - 1)].values()) if dp[(m - 1, n - 1)].values() else -1
