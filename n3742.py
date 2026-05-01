class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [{} for _ in range(n)]
        dp[0] = {k : 0}

        for x in range(m):
            if grid[x][0] != 0:
                updated = {}
                for key, value in dp[0].items():
                    if key > 0:
                        updated[key - 1] = value + grid[x][0]
                dp[0] = updated
            for y in range(1, n):
                top = dp[y]
                left = dp[y - 1]
                updated = {}
                for key in (top.keys() | left.keys()):
                    if grid[x][y] == 0:
                        updated[key] = max(top.get(key, 0), left.get(key, 0))
                    elif key > 0:
                        updated[key - 1] = max(top.get(key, 0), left.get(key, 0)) + grid[x][y]
                dp[y] = updated
        return max(dp[n - 1].values()) if dp[n - 1].values() else -1
