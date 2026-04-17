class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ALPH = ord('z') - ord('a') + 1
        n = len(s)
        incriments = [0] * (n + 1)
        for shift in shifts:
            direction = 1 if shift[2] == 1 else -1
            incriments[shift[0]] += direction
            incriments[shift[1] + 1] -= direction
        result = ""
        level = 0
        for i in range(n):
            level += incriments[i]
            result += chr((((ord(s[i]) - ord('a') + level) % ALPH) + ALPH) % ALPH + ord('a')) 
        return result
