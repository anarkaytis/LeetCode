class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0
        for i, c in enumerate(s):
            if int(c) != i % 2:
                cnt += 1
        return min(cnt, len(s) - cnt)
