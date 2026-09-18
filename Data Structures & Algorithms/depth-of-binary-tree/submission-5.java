/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    
    public int maxDepth(TreeNode root) {
        if(root == null)
            return 0;

        return depth(root, 1);
    }

    public int depth(TreeNode node, int depth) {
        // base
        if(node == null)
            return 0;

        // pre


        // recurse
        int leftDepth = depth(node.left, depth);
        int rightDepth = depth(node.right, depth);

        // post
        return 1 + Math.max(leftDepth, rightDepth);
    }

}
