class Solution:
    def clumsy(self, n: int) -> int:
        result = 0
        if n <= 2:
            return n
        if n >= 3:
            result = 2 * (n * (n - 1) // (n - 2))
        for i in range(n, 3, -4):
            result += (i - 3) - i * (i - 1) // (i - 2) 
        if n % 4 == 1:
            result -= 1
        elif n % 4 == 2:
            result -= 2
        elif n % 4 == 3:
            result -= 6
        return result
