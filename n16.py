class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        indexed = sorted(nums)
        prev = None
        best = indexed[0] + indexed[1] + indexed[2]
        for idx, goal in enumerate (indexed):
            if goal == prev:
                continue
            prev = goal
            l = idx + 1
            r = len(indexed) - 1
            while l < r:
                diff = indexed[l] + indexed[r] + goal - target
                if diff == 0:
                    return target
                if abs(best - target) > abs(diff):
                    best = indexed[l] + indexed[r] + goal
                elif diff < 0:
                    l += 1
                else:
                    r -= 1
        return best
