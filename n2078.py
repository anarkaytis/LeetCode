class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxD = 0
        n = len(colors)
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                maxD = i
                break
        for j in range(n):
            if colors[j] != colors[n - 1]:
                maxD = max(maxD, n - j - 1)
                break
        return maxD
