class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        sMin = nums[n - 1]
        result = total - sMin * 2
        for i in range(n - 1, 0, -1):
            total -= nums[i]
            sMin = min(sMin, nums[i])
            result = max(result, total - sMin)
        return result
