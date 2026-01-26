class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for i in range(len(magazine)):
            l = magazine[i]
            m[l] = m.get(l, 0) + 1
        for note in ransomNote:
            if m.get(note, 0) == 0:
                return False
            m[note] -= 1
        return True
