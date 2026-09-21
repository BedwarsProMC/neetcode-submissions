# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            # base case - found leaf node, all good so return True
            if not node:
                return True
            
            # BST property not respected so FALSE
            if not (left < node.val < right):
                return False

            # recursive case - update bounds as descend
            left = valid(node.left, left, node.val)
            right = valid(node.right, node.val, right)

            # post-recursion
            return left and right   

        return valid(root, float('-inf'), float('inf'))
