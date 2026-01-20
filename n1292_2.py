class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row = 0
            for j in range(n):
                row += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row
        result = 0
        for i in range(m):
            for j in range(n):
                for k in range(result + 1, min(m - i, n - j) + 1):
                    candidate = ps[i + k][j + k] + ps[i][j] - ps[i][j + k] - ps[i + k][j]
                    if candidate <= threshold:
                        result = k
        return result
