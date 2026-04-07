class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        n = len(nums)
        zeroes = nums[: ones].count(0)
        result = zeroes
        for i in range(n):
            if nums[i] == 0:
                zeroes -= 1
            if nums[(i + ones) % n] == 0:
                zeroes += 1
            result = min(result, zeroes)
        return result
