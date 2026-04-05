class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cntY, cntX = 0, 0
        for letter in moves:
            if letter == "U":
                cntY += 1
            elif letter == "D":
                cntY -= 1
            elif letter == "R":
                cntX += 1
            else:
                cntX -= 1
        return (cntY == 0) and (cntX == 0)
