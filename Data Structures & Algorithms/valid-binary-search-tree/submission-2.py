# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, low, high):
            # base case - stepped below a leaf node
            if not node:
                return True
            
            # PRE-RECURSION (work done on the way down)
            if not (low < node.val < high):
                return False

            # recursive case - tighten bounds as descend
            left_ok = valid(node.left, low, node.val)
            right_ok = valid(node.right, node.val, high)

            # POST-RECURSION (work done on the way back up)
            # only valid if both subtrees are also valid
            # False will poison and return False 
            return left_ok and right_ok   

        return valid(root, float('-inf'), float('inf'))
