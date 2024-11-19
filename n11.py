class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1 
        max_val = 0
        while l != r:
            if height[l] < height[r]:
                volume = height[l] * (r - l)
                l += 1
            else:
                volume = height[r] * (r - l)
                r -= 1
            if max_val < volume:
                max_val = volume
        return max_val
