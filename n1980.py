class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        unique = ""
        for i, num in enumerate(nums):
            unique += chr(1 ^ ord (num[i]))
        return unique
