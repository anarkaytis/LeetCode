class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = min(ranks) * cars * cars + 1 
        while l < r:
            mid = (l + r) // 2
            made = 0
            for rank in ranks:
                made += int((mid // rank) ** 0.5)
            if made < cars:
                l = mid + 1
            else:
                r = mid 
        return l
