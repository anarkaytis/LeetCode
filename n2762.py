class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total = 0
        l = 0
        cnt = {}

        for r in range(len(nums)):
            if len(cnt) != 0:
                low = min(cnt.keys())
                high = max(cnt.keys())

                if abs(nums[r] - low) > 2:
                    while low in cnt:
                        cnt[nums[l]] -= 1
                        if cnt[nums[l]] == 0:
                            del cnt[nums[l]]
                        l += 1

                if abs(nums[r] - high) > 2:
                    while high in cnt:
                        cnt[nums[l]] -= 1
                        if cnt[nums[l]] == 0:
                            del cnt[nums[l]]
                        l += 1 

            cnt[nums[r]] = cnt.get(nums[r], 0) + 1
            total += r - l + 1
            
        return total    
