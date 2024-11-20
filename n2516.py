class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ALL_LETTERS = "abc"
        letters = {}
        if k == 0:
            return 0
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        for letter in ALL_LETTERS:
            if letters.get(letter, 0) < k:
                return -1
        l = 0
        total_k = 0
        letters.clear()
        while total_k != len(ALL_LETTERS):
            letters[s[l]] = letters.get(s[l], 0) + 1
            if letters[s[l]] == k:
                total_k += 1
            l += 1
        min_drop = l
        r = len(s) - 1
        for i in range(l - 1, -1, -1):
            letters[s[i]] -= 1
            while letters[s[i]] < k:
                letters[s[r]] += 1
                r -= 1
            min_drop = min(min_drop, i + len(s) - 1 - r)
        return min_drop 
