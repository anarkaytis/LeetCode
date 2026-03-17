class Solution:
    def binaryGap(self, n: int) -> int:
        if n & (n - 1) == 0:
            return 0
            
        nums = []
        while n != 0:
            nums.append(n & 1)
            n >>= 1
        i = 0
        while nums[i] == 0:
            i += 1

        soFar = 0
        result = 0
        for num in nums[i :]:
            if num == 0:
                soFar += 1
                result = max(result, soFar)
            else:
                soFar = 0
        return result + 1
