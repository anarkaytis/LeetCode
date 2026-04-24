class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = r = 0
        for move in moves:
            if move != 'R':
                l += 1
            else:
                l -= 1
        for move in moves:
            if move != 'L':
                r += 1
            else:
                r -= 1
        return max(l, r)
