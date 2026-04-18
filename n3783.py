class Solution:
    def mirrorDistance(self, n: int) -> int:
        num = n
        reverse = 0
        while num != 0:
            reverse = reverse * 10 + num % 10
            num //= 10
        return abs(n - reverse)
