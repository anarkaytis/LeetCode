class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
                1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        result = 0
        for i in range(left, right + 1):
            result += prime[i.bit_count()]
        return result
