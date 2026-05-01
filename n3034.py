class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        cnt0 = cnt1 = cnt_1 = 0
        n = len(nums)
        m = len(pattern)
        w = deque()

        for num in pattern:
            if num == 1:
                cnt1 += 1
            elif num == -1:
                cnt_1 += 1
            else:
                cnt0 += 1

        for i in range(m):
            v = 0
            if nums[i + 1] > nums[i]:
                v = 1
                cnt1 -= 1
            elif nums[i + 1] < nums[i]: 
                v = -1
                cnt_1 -= 1
            else:
                cnt0 -= 1
            w.append(v)

        result = 0
        if (cnt0 == 0) and (cnt1 == 0) and (cnt_1 == 0):
            if all(a == b for a, b in zip(w, pattern)):
                result += 1
        
        for i in range(m, n - 1):
            v = 0
            if nums[i + 1] > nums[i]:
                v = 1
                cnt1 -= 1
            elif nums[i + 1] < nums[i]: 
                v = -1
                cnt_1 -= 1
            else:
                cnt0 -= 1
            elem = w.popleft()
            w.append(v)
            if elem == 1:
                cnt1 += 1
            elif elem == -1:
                cnt_1 += 1
            else:
                cnt0 += 1
            if (cnt0 == 0) and (cnt1 == 0) and (cnt_1 == 0):
                if all(a == b for a, b in zip(w, pattern)):
                    result += 1
        return result
