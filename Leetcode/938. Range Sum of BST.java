
  // Definition for a binary tree node.
  // public class TreeNode {
  //     int val;
  //     TreeNode left;
  //     TreeNode right;
  //     TreeNode(int x) { val = x; }
  // }

  class Solution {
    int sum;
    public int rangeSumBST(TreeNode root, int L, int R) {
        sum = 0;
        traverse(root,L,R);
        return sum;
    }
    public void traverse(TreeNode b, int L, int R)
    {
        if(b!=null)
        {
            if(L <= b.val && b.val <= R)
                sum = sum + b.val;
            if (L < b.val)
                traverse(b.left,L,R);
            if (b.val < R)
                traverse(b.right,L,R);
        }
    }
}