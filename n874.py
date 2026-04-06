class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        obstacle_unique = set()
        for obstacle in obstacles:
            obstacle_unique.add((obstacle[0], obstacle[1]))
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        max_dist = 0

        for command in commands:
            if command == -2:
                direction_idx = (direction_idx + 3) % 4
            elif command == -1:
                direction_idx = (direction_idx + 1) % 4
            else:
                for i in range(command):
                    x1 = x + direction[direction_idx][0]
                    y1 = y + direction[direction_idx][1]
                    if (x1, y1) in obstacle_unique:
                        break
                    x, y = x1, y1
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist
