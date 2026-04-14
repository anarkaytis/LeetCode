class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        if b in a + a:
            return 2
        
        idx = b.find(a)
        if idx == -1:
            return -1

        if (idx != 0) and (b[:idx] != a[-idx:]):
            return -1
        nB = len(b)
        nA = len(a)
 
        for i in range(idx, nB - nA, nA):
            if b[i : i + nA] != a:
                return -1
        
        tail = (nB - idx) % nA
        if (tail != 0) and (b[-tail:] != a[:tail]):
            return -1

        result = (nB - idx) // nA
        if tail != 0:
            result += 1
        if idx != 0:
            result += 1
        return result
