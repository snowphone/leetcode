/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node inorderSuccessor(Node node) {
        if (node.right != null) {
            return goLeft(node.right);
        }
        return goUp(node, node.val);
    }

    private Node goLeft(Node root) {
        if (root.left == null) {
            return root;
        }
        return goLeft(root.left);
    }
    
    private Node goUp(Node root, int target) {
        if (root == null) {
            return root;
        }
        if (target < root.val) {
            return root;
        }
        return goUp(root.parent, target);
    }
}