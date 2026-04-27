from enum import Enum

class Direction(Enum):
    EAST = 0
    WEST = 1
    NORTH = 2
    SOUTH = 3
class Turn(Enum):
    WEST_EAST = 1
    NORTH_SOUTH = 2
    WEST_SOUTH = 3
    EAST_SOUTH = 4
    WEST_NORTH = 5
    EAST_NORTH = 6
    
class Solution:
    def hasValidPathFrom(self, dir: Direction) -> bool:
        x = y = 0
        m = len(self.grid)
        n = len(self.grid[0])

        while True:
            x_ = x
            y_ = y
            match Turn(self.grid[y][x]):
                case Turn.WEST_EAST:
                    if dir == Direction.WEST:
                        x += 1
                    elif dir == Direction.EAST:
                        x -= 1
                    else:
                        return False
    
                case Turn.NORTH_SOUTH:
                    if dir == Direction.NORTH:
                        y += 1
                    elif dir == Direction.SOUTH:
                        y -= 1
                    else:
                        return False

                case Turn.WEST_SOUTH:
                    if dir == Direction.WEST:
                        y += 1
                        dir = Direction.NORTH
                    elif dir == Direction.SOUTH:
                        x -= 1
                        dir = Direction.EAST
                    else:
                        return False

                case Turn.EAST_SOUTH:
                    if dir == Direction.EAST:
                        y += 1
                        dir = Direction.NORTH
                    elif dir == Direction.SOUTH:
                        x += 1
                        dir = Direction.WEST
                    else:
                        return False

                case Turn.WEST_NORTH:
                    if dir == Direction.WEST:
                        y -= 1
                        dir = Direction.SOUTH
                    elif dir == Direction.NORTH:
                        x -= 1
                        dir = Direction.EAST
                    else:
                        return False

                case Turn.EAST_NORTH:
                    if dir == Direction.EAST:
                        y -= 1
                        dir = Direction.SOUTH
                    elif dir == Direction.NORTH:
                        x += 1
                        dir = Direction.WEST
                    else:
                        return False

            if (x_ == n - 1) and (y_ == m - 1):
                return True
            if (x == 0) and (y == 0):
                return False
            if (x < 0) or (y < 0) or (x >= n) or (y >= m):
                return False
        return False

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.grid = grid
        match Turn(self.grid[0][0]):
            case Turn.WEST_EAST:
                return self.hasValidPathFrom(Direction.WEST)
            case Turn.NORTH_SOUTH:
                return self.hasValidPathFrom(Direction.NORTH)
            case Turn.WEST_SOUTH:
                return self.hasValidPathFrom(Direction.WEST)
            case Turn.EAST_SOUTH:
                return self.hasValidPathFrom(Direction.EAST) or self.hasValidPathFrom(Direction.SOUTH)
            case Turn.WEST_NORTH:
                return False
            case Turn.EAST_NORTH:
                return self.hasValidPathFrom(Direction.NORTH)
        return False
