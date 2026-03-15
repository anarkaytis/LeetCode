class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        maxRight = []
        n = len(grid)
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    break
            maxRight.append((j, i))
        maxRight.sort()

        for i in range(n):
            if maxRight[i][0] > i:
                return -1

        for i in range(n):
            minIdx = i
            for j in range(i + 1, n):
                if maxRight[j][0] > i:
                    break
                if maxRight[j][1] < maxRight[minIdx][1]:
                    minIdx = j
            temp = maxRight[minIdx]
            for j in range(minIdx, i, -1):
                maxRight[j] = maxRight[j - 1]
            maxRight[i] = temp

        idx = [i for i in range(n)]
        result = 0
        for i in range(n):
            row = maxRight[i][1]
            result += idx[row] - i
            for j in range(row):
                idx[j] += 1
        return result
