class Solution:
    MOD = 1000000000 + 7
    def dfs(self, g: dict[tuple[int, int]], idx: int, result: List[int]) -> None:
        if idx not in g:
            return

        for child, weight in g[idx]:
            result[child] = weight * result[idx] % self.MOD
            self.dfs(g, child, result)

    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        n = len(conversions)
        g = {}
        for unit in conversions:
            soFar = g.get(unit[0], [])
            soFar.append((unit[1], unit[2]))
            g[unit[0]] = soFar
        result = [0] * (n + 1)
        result[0] = 1
        self.dfs(g, 0, result)
        return result
