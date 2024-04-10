#include <algorithm>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
 public:
    int result = 0;
    int dfs(TreeNode* root) {
        if (!root) {
            return 0;
        }
        // return max path sum without split
        int leftMax = dfs(root->left);
        int rightMax = dfs(root->right);
        leftMax = std::max(leftMax, 0);
        rightMax = std::max(rightMax, 0);

        // compute max path sum with split
        result = std::max(result, (root->val + leftMax + rightMax));

        return root->val + std::max(leftMax, rightMax);
    }
    int maxPathSum(TreeNode* root) {
        if (!root) {
            return 0;
        }
        result = root->val;
        dfs(root);
        return result;
    }
};
