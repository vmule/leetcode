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
    void dfs(TreeNode* node, int val, int depth, int cur_depth) {
        if (depth == 1) {
            auto new_root = new TreeNode(node->val, node->left, node->right);
            node->val = val;
            node->left = new_root;
            node->right = nullptr;
            return;
        }

        if (cur_depth == (depth - 1)) {
            auto left_tmp = node->left;
            auto right_tmp = node->right;

            node->left = new TreeNode(val, left_tmp, nullptr);
            node->right = new TreeNode(val, nullptr, right_tmp);
            return;
        }

        ++cur_depth;
        if (cur_depth < depth) {
            if (node->left) {
                dfs(node->left, val, depth, cur_depth);
            }
            if (node->right) {
                dfs(node->right, val, depth, cur_depth);
            }
        }
    }

    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        dfs(root, val, depth, 1);
        return root;
    }
};
