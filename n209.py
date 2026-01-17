class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                result = min(result, r - l)
                sum -= nums[l]
                l += 1
        return result + 1 if (result != len(nums) + 1) else 0
