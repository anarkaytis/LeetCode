class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        y = n ^ ( n >> 1)
        return (y & (y + 1)) == 0
