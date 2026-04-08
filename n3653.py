class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000000 + 7
        for q in queries:
            for idx in range(q[0], q[1] + 1, q[2]):
                nums[idx] = (nums[idx] * q[3]) % MOD
        result = 0
        for num in nums:
            result ^= num
        return result
