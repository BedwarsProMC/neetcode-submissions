# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def dfs(p, q):
            if not self.same: # early exist
                return

            # 1. base case
            if not p and not q: # both nodes are null so thats fine
                return
            
            # 2. recursive case

            # pre recursion
            if p and not q:
                self.same = False
                return

            if q and not p:
                self.same = False
                return

            if p and q and p.val != q.val:
                self.same = False

            # recurse
            dfs(p.left, q.left)
            dfs(p.right, q.right)

            # post recursion - no

        dfs(p, q)
        return self.same