class Robot:

    def __init__(self, width: int, height: int):
        self.x, self.y = 0, 0
        self.width  = width - 1
        self.height = height - 1
        self.directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.names = ["East", "South", "West", "North"]
        self.current = 0
        
    def step(self, num: int) -> None:
        dx, dy = 0, 0
        while True:
            dx = self.directions[self.current][0] * num
            dy = self.directions[self.current][1] * num
            if ((self.x + dx >= 0) and (self.x + dx <= self.width)) and ((self.y + dy >= 0) and(self.y + dy <= self.height)):
                break

            if dx > 0:
                num -= self.width - self.x
                self.x = self.width
            elif dx < 0:
                num -= self.x
                self.x = 0
            elif dy > 0:
                num -= self.height - self.y
                self.y = self.height
            elif dy < 0:
                num -= self.y
                self.y = 0

            if (self.x == 0) and (self.y == 0) and (self.current == 1):
                num %= (self.width + self.height) * 2
            if num != 0:
                self.current = (self.current + 3) % 4
            
        self.x += dx
        self.y += dy

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        
    def getDir(self) -> str:
        return self.names[self.current]
