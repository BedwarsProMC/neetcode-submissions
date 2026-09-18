# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            # 1. base case
            if not node:
                return 0

            # 2. recursive case

            # no pre case

            # recurse
            left = dfs(node.left)
            right = dfs(node.right)

            # post case
            diameter = left + right
            nonlocal res
            res = max(res, diameter)
            height = 1 + max(left, right)

            return height

        dfs(root)
        return res

        