class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp0 = [[0] * n for _ in range(m)]
        dp1 = [[0] * n for _ in range(m)]
        dp2 = [[0] * n for _ in range(m)]
        dp0[0][0] = coins[0][0]
        dp1[0][0] = max(0, coins[0][0])
        dp2[0][0] = max(0, coins[0][0])

        for i in range(1, m):
            dp0[i][0] = dp0[i - 1][0] + coins[i][0]
            dp1[i][0] = max(dp0[i - 1][0], coins[i][0] + dp1[i - 1][0])
            dp2[i][0] = max(dp1[i - 1][0], coins[i][0] + dp2[i - 1][0])
        for j in range(1, n):
            dp0[0][j] = dp0[0][j - 1] + coins[0][j]
            dp1[0][j] = max(dp0[0][j - 1], coins[0][j] + dp1[0][j - 1])
            dp2[0][j] = max(dp1[0][j - 1], coins[0][j] + dp2[0][j - 1])
        
        for i in range(1, m):
            for j in range(1, n):
                dp0[i][j] = max(dp0[i - 1][j], dp0[i][j - 1]) + coins[i][j]
                dp1[i][j] = max(dp0[i - 1][j], dp0[i][j - 1], coins[i][j] + dp1[i - 1][j], coins[i][j] + dp1[i][j - 1])
                dp2[i][j] = max(dp1[i - 1][j], dp1[i][j - 1], coins[i][j] + dp2[i - 1][j], coins[i][j] + dp2[i][j - 1])
        
        return max(dp0[m - 1][n - 1], dp1[m - 1][n - 1], dp2[m - 1][n - 1])
