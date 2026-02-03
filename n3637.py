class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[n - 2] >= nums[n - 1]:
            return False
        if nums[0] >= nums[1]:
            return False
        change_dir = 0
        increasing = True
        for i in range(2, n):
            if nums[i] == nums[i - 1]:
                return False
            next_increasing = (nums[i] > nums[i - 1])
            if increasing != next_increasing:
                change_dir += 1
            increasing = next_increasing
        return change_dir == 2
