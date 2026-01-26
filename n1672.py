class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        w = 0
        m = len(accounts)
        n = len(accounts[0])
        for i in range(m):
            i_w = 0
            for j in range(n):
                i_w += accounts[i][j]
            w = max(w, i_w)
        return w
