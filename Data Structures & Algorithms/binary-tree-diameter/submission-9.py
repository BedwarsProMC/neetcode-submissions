# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node): # return depth
            # base case
            if not node:
                return 0
            
            # recursive case
            left = dfs(node.left)
            right = dfs(node.right)

            # post-recursion
            nonlocal res
            res = max(res, left + right)
            depth = 1 + max(left, right)

            return depth

        dfs(root)
        return res