class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            unique = set()
            cnt = [0, 0]
            for j in range(i, n):
                if nums[j] not in unique:
                    unique.add(nums[j])
                    cnt[nums[j] & 1] += 1
                if cnt[0] == cnt[1]:
                    result = max(result, j - i + 1)
            if i >= n - result:
                break
        return result
