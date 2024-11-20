class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        unique = set()
        l = 0
        sum_all = 0
        max_sum = 0
        for r, num in enumerate(nums):
            if num not in unique:
                unique.add(num)
                sum_all += num
            else:
                while nums[l] != num:
                    unique.remove(nums[l])
                    sum_all -= nums[l]
                    l += 1
                l += 1
            if r - l == k - 1:
                max_sum = max(max_sum, sum_all)
                unique.remove(nums[l])
                sum_all -= nums[l]
                l += 1
        return max_sum
