class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        result = 0

        while len(nums) > 1:
            sorted = True
            min_pair = float("inf")
            idx = -1
            for i in range(len(nums) - 1):
                pair = nums[i] + nums[i + 1]
                if nums[i] > nums[i + 1]:
                    sorted = False
                if pair < min_pair:
                    min_pair = pair
                    idx = i
            if sorted:
                break
            result += 1
            nums[idx] = min_pair
            nums.pop(idx + 1)

        return result 
