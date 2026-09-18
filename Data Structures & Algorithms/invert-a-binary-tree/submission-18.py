# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. base case
        if not root:
            return None
        
        # 2. recursive case
        
        # pre
        root.left, root.right = root.right, root.left

        # recursuve
        self.invertTree(root.left)
        self.invertTree(root.right)

        # post

        return root
        