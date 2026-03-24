class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = 0
        cntNeg = 0
        minAbs = 100000
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] > 0:
                    sum += matrix[i][j]
                else:
                    sum -= matrix[i][j]
                    cntNeg += 1
                minAbs = min(minAbs, abs(matrix[i][j]))
        
        if (cntNeg & 1) != 0:
            sum -= minAbs * 2
        
        return sum
