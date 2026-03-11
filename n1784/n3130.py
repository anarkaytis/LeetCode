class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000000 + 7
        ps0 = [[0] * (one + 1) for _ in range(zero + 1)]
        ps1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(1, min(limit, zero) + 1):
            ps0[i][0] = 1
        for i in range(1, min(limit, one) + 1):
            ps1[0][i] = 1

        for z in range(1, zero + 1):
            for o in range(1, one + 1):
                s0 = ps1[z - 1][o]
                if z > limit:
                    s0 -= ps1[z - limit - 1][o]
                ps0[z][o] = ps0[z][o - 1] + s0 % MOD

                s1 = ps0[z][o - 1]
                if o > limit:
                    s1 -= ps0[z][o - limit - 1]
                ps1[z][o] = ps1[z - 1][o] + s1 % MOD
        return (ps0[zero][one] - ps0[zero][one - 1] + ps1[zero][one] - ps1[zero - 1][one]) % MOD
