class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
            else:
                count = 0
                x = num
                while x % 2 == 1:
                    x >>= 1
                    count += 1
                num ^= 1 << (count - 1)
                result.append(num)
        return result
