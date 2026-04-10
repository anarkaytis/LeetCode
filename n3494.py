class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        free = [0] * n
        for m in mana:
            now = free[0]
            for i in range(1, n):
                now = max(free[i], now + skill[i - 1] * m)
            free[n - 1] = now + skill[n - 1] * m
            for i in range(n - 2, -1, -1):
                free[i] = free[i + 1] - skill[i + 1] * m
        return free[n - 1]        
