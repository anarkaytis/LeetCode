class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        for a, b in adjacentPairs:
            neighbors[a].append(b)
            neighbors[b].append(a)
        start = 0
        for candidate, neighbor in neighbors.items():
            if len(neighbor) == 1:
                start = candidate
                break
        result = [start]
        prev = None
        n = len(adjacentPairs)
        for _ in range(n):
            for neighbor in neighbors[start]:
                if neighbor != prev:
                    result.append(neighbor)
                    prev = start
                    start = neighbor
                    break
        return result
