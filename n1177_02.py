class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        alph = [0]
        result = []

        for letter in s:
            alph.append(alph[-1] ^ ( 1 << (ord(letter) - ord('a'))))
        
        for query in queries:
            cntOdd = (alph[query[1] + 1] ^ alph[query[0]]).bit_count()
            cntOdd -= (query[1] - query[0] - 1) & 1
            result.append(cntOdd <= (2 * query[2]))

        return result
