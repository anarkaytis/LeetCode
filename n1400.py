class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        freq = {}
        odd = 0
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
        for count in freq.values():
            if count % 2 == 1:
                odd += 1
        return (k >= odd)
