class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        result = 0
        for num in nums:
            x = num
            while x in unique:
                unique.remove(x)
                x += 1
            y = num - 1
            while y in unique:
                unique.remove(y)
                y -= 1
            result = max(result, x - y - 1)
        return result
