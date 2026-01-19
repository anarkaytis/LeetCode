class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        head = 0
        prev = None
        for i in range(len(nums)):
            num = nums[i]
            if num == prev:
                duplicates += 1
            else:
                duplicates = 0
            if duplicates < 2:
                nums[head] = num
                head += 1
            prev = num
        return head 
