class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            freq = [0] * (ord("z") - ord("a") + 1)
            max_freq = 0
            distinct = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord("a")
                freq[idx] += 1
                if freq[idx] == 1:
                    distinct += 1
                max_freq = max(max_freq, freq[idx])
                if (j - i + 1) == max_freq * distinct:
                    result = max(result, j - i + 1)
            if i >= n - result:
                break
        return result
