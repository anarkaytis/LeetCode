class Solution:
    def doableHeight(self, time: int, workerTimes: List[int]) -> int:
        sumH = 0
        for workerTime in workerTimes:
            sumH += int(((sqrt(1 + 8 * time // workerTime)) - 1) / 2)
        return sumH
            
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        r = (mountainHeight * (mountainHeight + 1) // 2) * min(workerTimes) + 1
        l = 1
        while l < r:
            mid = (l + r) // 2
            if self.doableHeight(mid, workerTimes) >= mountainHeight:
                r = mid
            else:
                l = mid + 1
        return l 
