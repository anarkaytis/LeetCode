class Solution:
    def minOperations(self, nums: List[int]) -> int:
        vals = {}
        for val in nums:
            vals[val] = vals.get(val, 0) + 1
        result = 0
        for val in vals.values():
            if val == 1:
                return -1
            result += val // 3
            if (val % 3) != 0:
                result += 1
        return result
