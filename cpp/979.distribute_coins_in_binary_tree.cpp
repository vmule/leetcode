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
    int result = 0;
public:
    int distributeCoins(TreeNode* root) {
        dfs(root);
        return result;
    }

private:
    int dfs(TreeNode* node)  {
        if (!node) {
            return 0;
        }
        int extra_coins = (node->val - 1) + dfs(node->left) + dfs(node->right);
        result += std::abs(extra_coins);
        return extra_coins;
    }
};
