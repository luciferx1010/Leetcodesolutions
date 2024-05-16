/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool helper(TreeNode* root) {
        ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
        // Base case: if the value of the node is 0 or 1, return true if it's 1, otherwise false
        if (root->val == 0 || root->val == 1)
            return root->val == 1;
        // If the value of the node is 2, evaluate its left or right subtree
        else if (root->val == 2)
            return helper(root->left) || helper(root->right);
        // If the value of the node is 3, evaluate both its left and right subtrees
        else if (root->val == 3)
            return helper(root->left) && helper(root->right);

        return false; // Return false if the value of the node is not in the expected range
    }

    // Method to evaluate the entire binary tree
    bool evaluateTree(TreeNode* root) {
        return helper(root); // Call the helper function to evaluate the tree
    }
};