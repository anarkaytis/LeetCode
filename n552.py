class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000000 + 7
        a0l0 = 1
        a0l1 = a0l2 = a1l0 = a1l1 = a1l2 = 0
        for _ in range(n):
            _a1l0 = a1l0
            a1l0 = (a1l0 + a1l1 + a1l2 + a0l0 + a0l1 + a0l2) % MOD
            a1l2 = a1l1
            a1l1 = _a1l0

            _a0l0 = a0l0
            a0l0 = (a0l0 + a0l1 + a0l2) % MOD
            a0l2 = a0l1
            a0l1 = _a0l0

        return (a0l0 + a0l1 + a0l2 + a1l0 + a1l1 + a1l2) % MOD
