class Solution:
    def check(self, nums: List[int], x: int) -> int:
        k = i = 0
        while i < len(nums):
            if nums[i] <= x:
                k += 1
                i += 1
            i += 1
        return k

    def minCapability(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = max(nums) + 1
        while l < r:
            m = (l + r) // 2
            if self.check(nums, m) < k:
                l = m + 1
            else:
                r = m
        return l 
