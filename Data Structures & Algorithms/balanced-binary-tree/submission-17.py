# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node): # returns depth
            # 1. base case
            if not node:
                return 0
            
            if not self.balanced:
                return 0

            # 2. recursive case

            # pre - none

            # recursive case
            left = dfs(node.left)
            right = dfs(node.right)
            
            # post-recursion
            diff = right - left
            if abs(diff) > 1:
            # if diff > 1 or diff < -1:
                self.balanced = False
            
            depth = 1 + max(left, right)
            return depth

        dfs(root)
        return self.balanced