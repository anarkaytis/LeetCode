class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ALPH_SIZE = 26
        n = len(s)
        alph = [[0] * (ALPH_SIZE)]
        result = []

        for i in range(n):
            alph.append(alph[i].copy())
            alph[-1][ord(s[i]) - ord('a')] += 1
        
        for query in queries:
            cntOdd = 0
            for i in range(ALPH_SIZE):
                cntOdd += (alph[query[1] + 1][i] - alph[query[0]][i]) & 1
            cntOdd -= (query[1] - query[0] - 1) & 1
            result.append(cntOdd <= (2 * query[2]))

        return result
