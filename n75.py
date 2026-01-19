class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for i in range(len(nums)):
            counts[nums[i]] += 1
        head = 0
        for i, cnt in enumerate(counts):
            for k in range(cnt):
                nums[head] = i
                head += 1
