# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        
        # base case
        if not node:
            return 0

        # no pre work

        # recusrive case
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        # post recursion
        height = 1 + max(left, right)
        return height

