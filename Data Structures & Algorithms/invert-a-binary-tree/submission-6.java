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
    public TreeNode invertTree(TreeNode root) {
        if(root == null)
            return root;

        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);

        while(!queue.isEmpty()) {

            TreeNode current = queue.poll();

            // swap left and right
            TreeNode left = current.left;
            TreeNode right = current.right;

            current.left = right;
            current.right = left;
            
            if(current.left != null)
                queue.add(current.left);

            if(current.right != null)
                queue.add(current.right);
        }
        return root;
    }

}
