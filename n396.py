class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        f = 0
        for i, num in enumerate(nums):
            f += i * num
        sumN = sum(nums)
        result = f
        for i in range(n - 1, 0, -1):
            f += sumN - n * nums[i]
            result = max(result, f)
        return result
