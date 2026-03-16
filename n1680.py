class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1000000000 + 7
        result = 1
        for i in range(2, n + 1):
            result = ((result << i.bit_length()) + i) % MOD
        return result
