class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = []
        for row in grid:
            for elem in row:
                l.append(elem)
        l.sort()
        min_ = l[0]
        n = len(l)
        for i in range(n):
            if (l[i] - min_) % x != 0:
                return -1
            l[i] = (l[i] - min_) // x
        pivot = l[n // 2]
        result = 0
        for elem in l:
            result += abs(elem - pivot)
        return result
