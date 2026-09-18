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
    public boolean isBalanced(TreeNode root) {
        boolean[] res = new boolean[]{true};
        dfs(root, res);
        return res[0];
    }

    private int dfs(TreeNode node, boolean[] res) {
        if(node == null)
            return 0;

        int left = dfs(node.left, res);
        int right = dfs(node.right, res);

        // if diff in height > 1, unbalanced
        int diff = left - right;
        if(diff > 1 || diff < -1)
            res[0] = false;

        return 1 + Math.max(left, right);
    }

    
}
