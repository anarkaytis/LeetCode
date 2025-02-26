class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_p = sum_n = 0
        for num in nums:
            if sum_p < 0:
                sum_p = 0
            sum_p += num
            if max_sum < sum_p:
                max_sum = sum_p

            if sum_n > 0: 
                sum_n = 0
            sum_n += num
            if max_sum < -sum_n:
                max_sum = -sum_n
        return max_sum 
