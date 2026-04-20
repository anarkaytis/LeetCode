class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = m_ = len(matrix)
        n = n_ = len(matrix[0])
        start = 0
        
        while (m_ > 0) and (n_ > 0):
            for j in range(start, n - start):
                result.append(matrix[start][j])
            for i in range(start + 1, m - start):
                result.append(matrix[i][-start - 1])
            if m_ > 1:
                for j in range(n - start - 2, start - 1, -1):
                    result.append(matrix[-start - 1][j])
            if n_ > 1:
                for i in range(m - start - 2, start, -1):
                    result.append(matrix[i][start])
            start += 1
            m_ -= 2
            n_ -= 2

        return result
