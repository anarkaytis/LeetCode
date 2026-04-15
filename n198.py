class Solution:
    def rob(self, nums: List[int]) -> int:
        max0 = max1 = 0
        for num in nums:
            _max1 = max1
            max1 = max0 + num
            max0 = max(max0, _max1)
        return max(max0, max1)
