class Solution:
    def canJump(self, nums: List[int]) -> bool:
        path = 0
        for num in nums:
            if path < 0:
                return False
            path = max(path, num) - 1
        return True
