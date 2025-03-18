class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        bitwise_or = 0
        longest = 0
        for r, num in enumerate(nums):
            while (bitwise_or & num != 0):
                bitwise_or ^= nums[l]
                l += 1
            bitwise_or |= num
            if longest < r - l:
                longest = r - l
        return longest + 1
