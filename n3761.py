class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        lastSeen = {}
        result = n
        for i in range(n):
            num = nums[i]
            if num in lastSeen:
                result = min(result, i - lastSeen[num])

            reverse = 0
            while num != 0:
                reverse = reverse * 10 + num % 10
                num //= 10
            lastSeen[reverse] = i
        return result if result != n else -1
