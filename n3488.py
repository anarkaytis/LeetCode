class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        result = [n] * n
        lastSeen = {}
        for i in range(3 * n // 2):
            idx = i % n
            num = nums[idx]
            if num in lastSeen:
                dist = i - lastSeen[num]
                result[idx] = min(result[idx], dist)
                result[lastSeen[num] % n] = min(result[lastSeen[num] % n] , dist)
            lastSeen[num] = i
        return [-1 if result[q] == n else result[q] for q in queries]
