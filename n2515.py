class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        minD = n
        for i in range(n):
            if words[i] == target:
                minD = min(minD, (n + i - startIndex) % n, (n - i + startIndex) % n)
        return minD if minD != n else -1
