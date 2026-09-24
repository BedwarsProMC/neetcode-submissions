"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToCopy = {}

        def dfs(node):
            # base case: already cloned, so return clone over making a new copy
            if node in oldToCopy:
                return oldToCopy[node]

            # pre-recursion
            # pre-order work: create copy and register it HERE b4 recusing. then any cycle hits base case.
            copy = Node(node.val)
            oldToCopy[node] = copy

            for nei in node.neighbors:
                # recursive case

                # post-order work: wire returned node copy into this nodes neighbor list
                copy.neighbors.append(dfs(nei))

            # post-order work: return this nodes copy to the caller who attaches to its own neighbor list
            return copy

        return dfs(node)
        