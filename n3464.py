class Solution:
    def canFitK(self, dist: int) -> bool:
        n = len(self.linear)
        for i in range(n):
            prev = self.linear[i]
            cnt = 1
            for j in range(i + 1, n):
                if self.linear[j] - prev >= dist:
                    prev = self.linear[j]
                    cnt += 1
                    if cnt == self.k:
                        break
            if (cnt == self.k) and (4 * self.side + self.linear[i] - prev >= dist):
                return True
            if 4 * self.side + self.linear[i] - self.linear[-1] >= dist:
                break
        return False

    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        self.side = side
        self.k = k
        self.linear = []
        for point in points:
            if point[0] == 0:
                self.linear.append(point[1])
            elif (point[1] == side):
                self.linear.append(self.side + point[0])
            elif (point[0] == side):
                self.linear.append(3 * self.side - point[1])
            else:
                self.linear.append(4 * self.side - point[0])
        self.linear.sort()
        l = 1
        r = (4 * self.side + self.k - 1) // self.k + 1
        while l < r:
            m = (l + r) // 2
            if self.canFitK(m):
                l = m + 1
            else:
                r = m
        return l - 1
