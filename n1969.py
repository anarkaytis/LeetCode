class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1000000000 + 7
        result = (1 << p) - 1
        x = result - 1
        for _ in range(p - 1):
            result = (result * x) % MOD 
            x = (x * x) % MOD
        return result
