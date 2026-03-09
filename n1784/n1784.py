class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 1
        n = len(s)
        while (i < n) and (s[i] == "1"):
            i += 1         
        for k in range(i, n):
            if s[k] == "1":
                return False
        return True
