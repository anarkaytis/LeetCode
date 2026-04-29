class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nh = 0
        hold = -1001
        cool = 0
        for price in prices:
            _hold = hold
            _cool = cool
            hold = max(hold, nh - price)
            cool = max(cool, _hold + price)
            nh = max(nh, _cool)
        return max(nh, cool)
