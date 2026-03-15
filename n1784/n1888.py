class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n
        sum = 0
        for i in range(n):
            prefix[i] = sum
            sum += (ord(s[i]) - ord("0")) ^ (i & 1)
        result = min(sum, n - sum)
        if (n & 1) == 0:
            return result
        
        sum = 0
        for i in range(n - 1, -1, -1):
            sum += (ord(s[i]) - ord("0")) ^ (i & 1)
            result = min(result, sum + i - prefix[i], n - i - sum + prefix[i])
        return result
