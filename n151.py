class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        words = [word for word in words if words != '']
        return ' '.join(words)
