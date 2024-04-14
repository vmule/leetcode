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
    int sum = 0;
    void dfs(TreeNode* node, bool left) {
        if (!node) {
            return;
        }

        if (left && !node->left && !node->right) {
            sum += node->val;
        }

        if (node->left) {
            dfs(node->left, true);
        }
        if (node->right) {
            dfs(node->right, false);
        }
    }

    int sumOfLeftLeaves(TreeNode* root) {
        dfs(root, false);
        return sum;
    }
};
