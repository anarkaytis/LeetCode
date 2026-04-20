class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if (nums[i] != i - 1) or (nums[i - 1] != i):
                    return False
        return True
