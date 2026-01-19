class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        max_size = 0
        for i in range(m):
            for j in range(n):
                sum = 0
                for k in range(0, min(m - i, n - j)):
                    sum += mat[i + k][j + k]
                    for r in range(k):
                        sum += mat[i + k][j + r] + mat[i + r][j + k]
                    if sum > threshold:
                        break
                    max_size = max(max_size, k + 1)
        return max_size
