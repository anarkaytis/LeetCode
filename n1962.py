class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        neg = [-x for x in piles]
        heapq.heapify(neg)
        for _ in range(k):
            maxP = heapq.heappop(neg)
            print(maxP)
            heapq.heappush(neg, -((1 - maxP) // 2))
        return -sum(neg) 
