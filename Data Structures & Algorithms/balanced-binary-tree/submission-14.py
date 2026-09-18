# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node) -> int:
            nonlocal res 
            
            if not res:
                return 0

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diff = left - right

            # if diff > 1 or diff < -1:
            if abs(diff) > 1:
                res = False

            return 1 + max(left, right)

        dfs(root)
        return res