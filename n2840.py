class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        cnt = [{}, {}] 
        for i, c in enumerate(s1):
            cnt[(i & 1)][c] = cnt[(i & 1)].get(c, 0) + 1
        for i, c in enumerate(s2):
            val = cnt[(i & 1)].get(c, 0)
            if val == 0:
                return False
            cnt[(i & 1)][c] = val - 1
        return True
