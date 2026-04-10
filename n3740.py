class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        first = {}
        second = {}
        n = len(nums)
        minD = n + 1
        for i in range(n):
            if nums[i] in first:
                minD = min(minD, i - first[nums[i]])
            if nums[i] in second:
                first[nums[i]] = second[nums[i]]
            second[nums[i]] = i
        return 2 * minD if minD != n + 1 else -1
