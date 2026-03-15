class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0] * n
        colums = [0] * m
        for i in range(n):
            for j in range(m):
                rows[i] += mat[i][j]
                colums[j] += mat[i][j]
        result = 0
        for i in range(n):
            if rows[i] != 1:
                continue
            for j in range(m):
                if colums[j] != 1:
                    continue
                result += mat[i][j]
        return result
