class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        count_y = 1
        hole_y = 1
        hBars = sorted(hBars)
        vBars = sorted(vBars)
        for i in range(len(hBars) - 1):
            if (hBars[i] + 1 == hBars[i + 1]):
                count_y += 1
            else:
                hole_y = max(count_y, hole_y)
                count_y = 1
        hole_y = max(count_y, hole_y)
        count_x = 1
        hole_x = 1
        for i in range(len(vBars) - 1):
            if (vBars[i] + 1 == vBars[i + 1]):
                count_x += 1
            else:
                hole_x = max(count_x, hole_x)
                count_x = 1
        hole_x = max(count_x, hole_x)
        size = min(hole_x, hole_y) + 1
        return size * size
