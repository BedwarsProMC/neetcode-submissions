# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same = self.sameTree(root, subRoot)
        if same:
            return True
        else:
            if root:
                left = self.isSubtree(root.left, subRoot)    
                right = self.isSubtree(root.right, subRoot)   

                return left or right

            return False

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

    