// ============================================
// 2196. Create Binary Tree From Descriptions
// ============================================
// Difficulty: Medium
//
// You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the **parent** of `child_i` in a **binary** tree of **unique** values. Furthermore,
//
// 	
// - If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`.
// 	
// - If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.
//
// Construct the binary tree described by `descriptions` and return *its **root***.
//
// The test cases will be generated such that the binary tree is **valid**.
//
//  
//
// **Example 1:**
//
// []
//
// **Input:** descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
// **Output:** [50,20,80,15,17,19]
// **Explanation:** The root node is the node with value 50 since it has no parent.
// The resulting binary tree is shown in the diagram.
//
// ```
//
// **Example 2:**
//
// []
//
// **Input:** descriptions = [[1,2,1],[2,3,0],[3,4,1]]
// **Output:** [1,2,null,null,3,4]
// **Explanation:** The root node is the node with value 1 since it has no parent.
// The resulting binary tree is shown in the diagram.
//
// ```
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= descriptions.length &lt;= 10^4`
// 	
// - `descriptions[i].length == 3`
// 	
// - `1 &lt;= parent_i, child_i &lt;= 10^5`
// 	
// - `0 &lt;= isLeft_i &lt;= 1`
// 	
// - The binary tree described by `descriptions` is valid.
//
// ====== SOLUTION ======

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
    public TreeNode createBinaryTree(int[][] descriptions) {
        HashMap<Integer, TreeNode> map = new HashMap<>();
        HashSet<Integer> children = new HashSet<>();

        for (int[] d : descriptions) {
            int parent = d[0];
            int child = d[1];
            int isLeft = d[2];

            map.putIfAbsent(parent, new TreeNode(parent));
            map.putIfAbsent(child, new TreeNode(child));

            if (isLeft == 1) {
                map.get(parent).left = map.get(child);
            } else {
                map.get(parent).right = map.get(child);
            }

            children.add(child);
        }

        for (int[] d : descriptions) {
            if (!children.contains(d[0])) {
                return map.get(d[0]);
            }
        }

        return null;
    }
}
