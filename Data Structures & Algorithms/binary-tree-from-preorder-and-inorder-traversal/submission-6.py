# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_idx = 0 # works along preorder array, as we building using preorder dfs. will be order of inserted nodes.

        indexes = {}
        for i, v in enumerate(inorder):
            indexes[v] = i
        
        def dfs(l, r):
            nonlocal root_idx

            if l > r:
                return None

            root = TreeNode(preorder[root_idx])
            root_idx += 1

            mid = indexes[root.val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        
        return dfs(0, len(inorder) - 1)