class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                break
        next_num = i
        for j in range(i + 1, len(nums)):
            if (nums[j] < nums[next_num]) and (nums[j] > nums[i - 1]):
                next_num = j
        swap = nums[i - 1]
        nums[i - 1] = nums[next_num]
        nums[next_num] = swap
        for num in sorted(nums[i:]):
            nums[i] = num
            i += 1
