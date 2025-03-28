class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        amount = {}
        for element in nums:
            amount[element] = amount.get(element, 0) + 1
            if 2 * amount[element] > len(nums):
                dominant = element
                break

        count = 0
        for element in nums:
            if element == dominant:
                count += 1

        left = 0
        for idx, val in enumerate(nums):
            if val == dominant:
                left += 1
            if (left * 2 > idx + 1) and ((count - left) * 2 > len(nums) - idx - 1):
                return idx
        return -1
