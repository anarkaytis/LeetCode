class Solution:
    def can_travel(self, stones: List[int], jump: int) -> bool:
        used = [False] * len(stones)
        current = 0
        for i in range(1, len(stones)):
            if stones[i] - stones[current] > jump:
                if i == current + 1:
                    return False
                current = i - 1
                used[current] = True
        current = len(stones) - 1
        for i in range(len(stones) - 2, -1, -1):
            if not used[i]:
                if stones[current] - stones[i] > jump:
                    return False
                current = i
        return True

    def maxJump(self, stones: List[int]) -> int:
        l = 1
        r = stones[len(stones) - 1] - stones[0] + 1
        while l < r:
            mid = (l + r) // 2
            if not self.can_travel(stones, mid):
                l = mid + 1
            else:
                r = mid
        return l 
