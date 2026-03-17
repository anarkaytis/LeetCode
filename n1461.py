class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n - k + 1 < (1 << k):
            return False
        window = 0
        for i in range(k):
            window = (window << 1) | (ord(s[i]) - ord("0"))
        unique = set([window])

        for i in range(k, n):
            window = (window << 1) | (ord(s[i]) - ord("0"))
            window &= (1 << k) - 1
            unique.add(window)
        return len(unique) == (1 << k)
