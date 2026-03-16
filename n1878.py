class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        maxR = []
        diag = min(m, n) // 2 + 1
        
        for x0 in range(m):
            for y0 in range(n):
                for d in range(diag):
                    sumR = 0
                    x1 = x0 - d
                    y1 = y0 + d
                    x2 = x0
                    y2 = y0 + 2 * d
                    x3 = x0 + d
                    y3 = y1
                    if (x1 < 0) or (y1 >= n) or (y2 >= n) or (x3 >= m):
                        break

                    for i in range(d):
                        sumR += grid[x0 - i][y0 + i] + grid[x1 + i][y1 + i] + grid[x2 + i][y2 - i] + grid[x3 - i][y3 - i]
                    if d == 0:
                        sumR = grid[x0][y0]

                    if sumR in maxR:
                        continue
                    if len(maxR) < 3:
                        maxR.append(sumR)
                    else:
                        minIdx = 0
                        for i in range(1, 3):
                            if maxR[i] < maxR[minIdx]:
                                minIdx = i
                        if maxR[minIdx] < sumR:
                            maxR[minIdx] = sumR

        maxR.sort(reverse=True)
        return maxR
