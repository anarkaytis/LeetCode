class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapify(heap)
        score = 0
        for _ in range(k):
            num = -heappop(heap)
            score += num
            heappush(heap, -((num + 2) // 3))
        return score 
