class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0 if n > 3 else True
