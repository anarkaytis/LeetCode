class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0
        for i in range(1, len(bottomLeft)):
            for j in range(0, i):
                x0 = max(bottomLeft[i][0], bottomLeft[j][0])
                x1 = min(topRight[i][0], topRight[j][0])
                if x1 <= x0:
                    continue
                y0 = max(bottomLeft[i][1], bottomLeft[j][1])
                y1 = min(topRight[i][1], topRight[j][1])
                if y1 <= y0:
                    continue
                max_side = max(max_side, min(x1 - x0, y1 - y0))
        return max_side * max_side
