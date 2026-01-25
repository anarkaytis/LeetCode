class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        k -= 1
        return min(nums[i + k] - nums[i] for i in range(len(nums) - k))
