class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        EPSILON = 1e-5
        min_b = squares[0][1]
        max_b = squares[0][1] + squares[0][2]
        total_a = 0
        for i in range(len(squares)):
            min_b = min(squares[i][1], min_b)
            max_b = max(squares[i][1] + squares[i][2], max_b)
            total_a += squares[i][2] * squares[i][2]
        while max_b - min_b > EPSILON:
            mid = (min_b + max_b) / 2
            above = 0
            for i in range(len(squares)):
                if squares[i][1] > mid:
                    above += squares[i][2] * squares[i][2]
                elif squares[i][1] + squares[i][2] > mid:
                    ratio = (squares[i][1] + squares[i][2] - mid) / squares[i][2]
                    above += squares[i][2] * squares[i][2] * ratio
            if above / total_a > 1/2:
                min_b = mid
            else:
                max_b = mid
        return min_b
