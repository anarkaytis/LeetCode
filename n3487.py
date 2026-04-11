class Solution:
    def maxSum(self, nums: List[int]) -> int:
        elements = set(nums)
        result = 0
        for elem in elements:
            if elem > 0:
                result += elem
        if result == 0:
            return max(elements)
        return result
