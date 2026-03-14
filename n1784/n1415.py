class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        k -= 1
        n -= 1
        next = [[1, 2], [0, 2], [0, 1]]
        idx = k // (1 << n)
        if idx > 2:
            return ""
        answer = "abc"[idx]
        k &= (1 << n) - 1
        for i in range(n - 1, -1, -1):
            idx = next[idx][(k >> i) & 1]
            answer += "abc"[idx]
        return answer
