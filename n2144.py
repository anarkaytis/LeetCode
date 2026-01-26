class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        cost.sort()
        result = 0
        for i in range(n - 1, -1, -3):
            if i - 1 >= 0:
                result += cost[i - 1]
            result += cost[i]
        return result
