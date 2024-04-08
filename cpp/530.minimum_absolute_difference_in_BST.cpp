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
    int last_value = std::numeric_limits<int>::max();
    int result = std::numeric_limits<int>::max();

    void dfs(TreeNode* node) {
        // in order traversal
        if (node->left) {
            dfs(node->left);
        }
        result = std::min(result, std::abs(last_value - node->val));
        last_value = node->val;

        if (node->right) {
            dfs(node->right);
        }
    }
    int getMinimumDifference(TreeNode* root) {
        dfs(root);
        return result;
    }
};
