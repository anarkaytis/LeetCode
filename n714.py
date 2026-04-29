class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        nh = 0
        hold = -50000
        for price in prices:
            _hold = hold
            hold = max(hold, nh - price)
            nh = max(nh, _hold + price - fee)
        return nh   
