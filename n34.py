class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        min = 0
        max = len(nums)
        start = 0
        fin = 0
        while min < max:
            mid = (min + max) // 2
            if nums[mid] < target:
                min = mid + 1
            else:
                max = mid
        start = min
        min = 0
        max = len(nums)
        while min < max:
            mid = (min + max) // 2
            if nums[mid] <= target:
                min = mid + 1
            else:
                max = mid
        fin = min 
        if start == fin:
            start = fin = -1
        else:
            fin -= 1
        return [start, fin]
