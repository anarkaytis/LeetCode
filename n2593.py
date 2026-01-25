class Solution:
    def findScore(self, nums: List[int]) -> int:
        num_sorted = sorted((num, idx) for idx, num in enumerate(nums))
        n = len(nums)
        score = 0
        state = [True] * n
        for num, idx in num_sorted:
            if not state[idx]:
                continue
            score += num
            if idx - 1 >= 0:
                state[idx - 1] = False
            if idx + 1 < n:
                state[idx + 1] = False
        return score
