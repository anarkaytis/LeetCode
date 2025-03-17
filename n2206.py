class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_pair = {}
        for num in nums:
            num_pair[num] = num_pair.get(num, 0) + 1
        for val in num_pair.values():
            if val % 2 != 0:
                return False
        return True
