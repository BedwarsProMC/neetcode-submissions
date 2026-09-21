# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if not root and not subRoot: # both nodes null so same tree.
            return True
        if not root: # root null, subtree NOT NULL, not same tree
            return False

        # pre recursion
        same = self.isSameTree(root, subRoot)
        if same:
            return True
        
        # recursive
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        # post recursion
        return left or right

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)