class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ps = {}
        ps[0] = 0
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            if prefix > x:
                break
            ps[prefix] = i + 1
        suffix = 0
        result = n + 1
        if x in ps:
            result = ps[x]
        for i in range(n - 1, -1, -1):
            suffix += nums[i]
            if suffix > x:
                break
            diff = x - suffix
            if diff in ps:
                result = min(result, ps[diff] + n - i)
        return result if result != n + 1 else -1
