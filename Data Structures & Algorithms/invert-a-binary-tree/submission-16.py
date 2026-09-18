# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # base case - hit a leaf node so stop recusive
        if not root:
            return None;

        # swap nodes
        temp = root.right
        root.right = root.left
        root.left = temp
      

        # recursive case - swap the two children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root