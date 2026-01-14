class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        length = len(nums)
        while (length > 0) and (nums[0] == nums[length - 1]):
            length -= 1
        if (length == 0):
            return target == nums[0]

        l = 0
        r = length
        while l < r:
            m = (l + r) // 2
            if nums[0] <= nums[m]:
                l = m + 1
            else:
                r = m 
        shift = l
        l = 0
        r = length
        while l < r:
            m = (l + r) // 2
            if target > nums[(m + shift) % length]:
                l = m + 1
            else:
                r = m 
        return target == nums[(l + shift) % length]
