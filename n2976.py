class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ALPHABET = 28
        INF = 28000000 + 1
        n = len(original)
        dest = [[INF] * ALPHABET for _ in range(ALPHABET)]
        for i in range(ALPHABET):
            dest[i][i] = 0
        for i in range(n):
            dest[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = min(dest[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')], cost[i])
        
        for k in range(ALPHABET):
            for i in range(ALPHABET):
                for j in range(ALPHABET):
                    if (dest[i][j] != 0) or (dest[i][j] != INF):
                        dest[i][j] = min(dest[i][j], dest[i][k] + dest[k][j])
        
        w = len(source)
        result = 0
        for i in range(w):
            if dest[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == INF:
                return -1
            result += dest[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        
        return result
