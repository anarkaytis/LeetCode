class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
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
            if target == nums[(m + shift) % length]:
                return (m + shift) % length
            elif target > nums[(m + shift) % length]:
                l = m + 1
            else:
                r = m 
        return -1
