class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False # a tree MUST have exactly n-1 edges to be at least valid.

        # tree must also be fully connectned and have no cycles

        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set() # used to detect cylces. and check we visited all n nodes (so graph is connected)
        
        def dfs(node, prevNode):
            if node in visited: # cycle detected 
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei, node):
                    return False

            return True


        return dfs(0, -1) and len(visited) == n