class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        h = [0] * n
        result = 0
        for i in range(m):
            for j in range(n):
                if (i != 0) and (matrix[i][j] != 0):
                    matrix[i][j] += matrix[i - 1][j]
                h[j] = matrix[i][j]
            h.sort(reverse = True)
            for j in range(n):
                result = max(result, h[j] * (j + 1))  
        return result    
