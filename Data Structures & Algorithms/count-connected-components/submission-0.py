class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        seen = set()
        num = 0

        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            if node in seen:
                return
            seen.add(node)

            for nei in adj[node]:
                dfs(nei)

        for node in range(n):
            if node not in seen:
                num += 1
                dfs(node)

        return num