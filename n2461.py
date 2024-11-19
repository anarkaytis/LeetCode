class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = 0 
        window_dict = {}
        duplicates = 0
        for i in range(k):
            window += nums[i]
            count = window_dict.get (nums[i], 0)
            window_dict[nums[i]] = count + 1
            if count == 1:
                duplicates += 1

        max_window = 0
        if duplicates == 0:
            max_window = window 
        
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k] 
            if window_dict[nums[i - k]] == 2:
                duplicates -= 1
            window_dict[nums[i - k]] -= 1
            window_dict[nums[i]] = window_dict.get (nums[i], 0) + 1
            if window_dict[nums[i]] == 2:
                duplicates += 1
            if duplicates == 0:
                max_window = max(max_window, window)
        return max_window
