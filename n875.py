class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            eaten = 0
            for pile in piles:
                eaten += (pile + mid - 1) // mid
            if eaten > h:
                l = mid + 1
            else:
                r = mid
        return l
