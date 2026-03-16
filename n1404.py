class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        result = n + 1
        if s[n - 1] == "0":
            while s[n - 1] == "0":
                n -= 1
        if n == 1:
            return result - 2

        for i in range(n):
            if s[i] == "0":
                result += 1
        return result 
