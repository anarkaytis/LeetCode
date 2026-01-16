class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        dy = set()
        dx = -1
        for i in range(len(hFences)):
            for j in range(i):
                dy.add(abs(hFences[i] - hFences[j]))

        for i in range(len(vFences)):
            for j in range(len(vFences) - 1, i, -1):
                size = abs(vFences[i] - vFences[j])
                if (size in dy):
                    dx = max(dx, size)
        return dx * dx % (1000000000 + 7) if dx > 0 else -1
