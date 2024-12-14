class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indexed = sorted(nums)
        total = []
        prev = None
        for idx, target in enumerate (indexed):
            if target == prev:
                continue
            prev = target
            l = idx + 1
            r = len(indexed) - 1
            while l < r:
                diff = indexed[l] + indexed[r] + target
                if diff == 0:
                    total.append([target, indexed[l], indexed[r]])
                    left_value = indexed[l]
                    while (l < r) and (indexed[l] == left_value):
                        l += 1
                    right_value = indexed[r]
                    while (l < r) and (indexed[r] == right_value):
                        r -= 1
                elif diff < 0:
                    l += 1
                else:
                    r -= 1
        return total
