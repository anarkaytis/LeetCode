class Solution:
    def minTime (self, start1: List[int], duration1: List[int], start2: List[int], duration2: List[int]) -> int:
        n = len(start1)
        m = len(start2)
        min1 = min(start1[i] + duration1[i] for i in range(n))
        return min(max(start2[i], min1) + duration2[i] for i in range(m))

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:   
        return min(self.minTime(landStartTime, landDuration, waterStartTime, waterDuration), self.minTime(waterStartTime, waterDuration, landStartTime, landDuration))
