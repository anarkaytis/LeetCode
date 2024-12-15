class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        indexed = sorted(nums)
        total = []
        prev_a = None
        for idx_a, val_a in enumerate (indexed):
            if val_a == prev_a:
                continue
            prev_a = val_a

            prev_b = None
            for idx_b in range(idx_a + 1, len(indexed)):
                val_b = indexed[idx_b]
                if val_b == prev_b:
                    continue
                prev_b = val_b

                l = idx_b + 1
                r = len(indexed) - 1
                while l < r:
                    diff = indexed[l] + indexed[r] + val_a + val_b - target
                    if diff == 0:
                        total.append([val_a, val_b, indexed[l], indexed[r]])
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
