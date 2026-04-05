class Solution:
    def integerBreak(self, n: int) -> int:
        maxProduct = 0

        for k in range(2, n):
            x = n // k
            candidate = x + (n % k)
            for i in range(k - 1):
                candidate *= x
            maxProduct = max(maxProduct, candidate)
            candidate = n % (x + 1)
            for i in range(n // (x + 1)):
                candidate *= x + 1
            maxProduct = max(maxProduct, candidate)
            
        return maxProduct
