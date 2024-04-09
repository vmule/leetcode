#include <vector>

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

// O(n) complexity, O(1) space
class Solution_1 {
 public:
    std::vector<TreeNode*> list{};

    TreeNode* dfs(TreeNode* root) {
        if (!root) {
            return nullptr;
        }
        TreeNode* leftTail = dfs(root->left);
        TreeNode* rightTail = dfs(root->right);

        if (root->left) {
            leftTail->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }

        TreeNode* last;
        if (rightTail) {
            last = rightTail;
        }
        if (!rightTail && leftTail) {
            last = leftTail;
        } else if (!leftTail && !rightTail) {
            last = root;
        }
        return last;
    }
    void flatten(TreeNode* root) { dfs(root); }
};

// O(n) complexity, O(n) space
class Solution_2 {
 public:
    std::vector<TreeNode*> list{};

    void dfs(TreeNode* node) {
        if (!node) {
            return;
        }
        list.push_back(node);
        if (node->left) {
            dfs(node->left);
        }
        if (node->right) {
            dfs(node->right);
        }
    }
    void flatten(TreeNode* root) {
        dfs(root);
        int len = list.size();
        for (int i = 1; i < len; ++i) {
            auto node = list[i];
            auto previous_node = list[i - 1];
            previous_node->left = nullptr;
            previous_node->right = node;
        }
    }
};
