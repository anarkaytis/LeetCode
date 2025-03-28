class Solution:
    def checkLine(self,rectangles: List[Tuple[int, int]]) -> int:
        sortedCoord = sorted(rectangles)
        last_coord = sortedCoord[0][1]
        count = 0
        for coord in sortedCoord:
            if coord[0] >= last_coord:
                count += 1
            if coord[1] > last_coord:
                last_coord = coord[1]
        return count

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        spans_x = [(x[0], x[2]) for x in rectangles ]
        if self.checkLine(spans_x) >= 2:
            return True
        spans_y = [(y[1], y[3]) for y in rectangles ]
        if self.checkLine(spans_y) >= 2:
            return True
        return False   
