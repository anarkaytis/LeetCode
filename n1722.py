class Solution:
    def dfs(self, group: List[int], groupIdx: int, idx: int) -> None:
        if group[idx] != 0:
            return
        group[idx] = groupIdx
        for dst in self.g[idx]:
            self.dfs(group, groupIdx, dst)

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        self.g = dict()
        for i in range(n):
            self.g[i] = [] 
        for swap in allowedSwaps:
            self.g[swap[0]].append(swap[1])
            self.g[swap[1]].append(swap[0])
            
        group = [0] * n
        groupIdx = 0
        for i in range(n):
            if group[i] == 0:
                groupIdx += 1
                self.dfs(group, groupIdx, i)

        src = {}
        dst = {}
        for i in range(n):
            d = src.get(group[i], {})
            d[source[i]] = d.get(source[i], 0) + 1
            src[group[i]] = d
            d = dst.get(group[i], {})
            d[target[i]] = d.get(target[i], 0) + 1
            dst[group[i]] = d

        total = 0
        for i in range(1, groupIdx + 1):
            for num, cnt in src[i].items():
                dstCnt = dst[i].get(num, 0)
                total += min(cnt, dstCnt)
        return n - total
