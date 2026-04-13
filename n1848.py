class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        minT = n
        for i in range(start, n):
            if nums[i] == target:
                minT = i - start
                break
        for i in range(start - 1, -1, - 1):
            if nums[i] == target:
                minT = min(minT, start - i)
                break
        return minT
