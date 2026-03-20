class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ABS = 2 * 100000 + 1
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for x in range(m - k + 1):
            for y in range(n - k + 1):
                values = [] 
                for i in range(k):
                    for j in range(k):
                        values.append(grid[x + i][y + j])
                values.sort()
                result = ABS
                for i in range(1, len(values)):
                    if values[i] - values[i - 1] == 0:
                        continue
                    result = min(result, values[i] - values[i - 1])
                if result == ABS:
                    result = 0
                ans[x][y] = result
        return ans
