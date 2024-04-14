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
    int total_sum = 0;

    void dfs(TreeNode* node, int sum) {
        if (!node) {
            return;
        }

        if (!node->right && !node->left) {
            total_sum += (sum + (node->val));
            return;
        }

        sum = (sum * 10) + (node->val * 10);
        dfs(node->left, sum);
        dfs(node->right, sum);
    }
    int sumNumbers(TreeNode* root) {
        dfs(root, 0);
        return total_sum;
    }
};
