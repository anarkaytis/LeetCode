class Solution:
    def dfs(self, node: int, graph: List[List[int]], visited: List[bool], companent: Dict[str, int]) -> None:
        if visited[node]:
            return
        companent["nodes"] += 1
        companent["edges"] += len(graph[node])
        visited[node] = True
        for neighbor in graph[node]:
            self.dfs(neighbor, graph, visited, companent)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range (n)]
        for edge in edges:
            graph[edge[1]].append(edge[0])
            graph[edge[0]].append(edge[1])
        
        visited = [False] * n
        result = 0
        for idx, visit in enumerate(visited):
            if not visit:
                companent = {"nodes" : 0, "edges" : 0}
                self.dfs(idx, graph, visited, companent)
                if companent["edges"] == companent["nodes"] * (companent["nodes"] - 1):
                    result += 1
        return result 
