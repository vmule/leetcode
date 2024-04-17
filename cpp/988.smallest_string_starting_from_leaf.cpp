#include <algorithm>
#include <string>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
 private:
    std::string dfs(TreeNode* node, std::string current_string = "") {
        if (!node) {
            return smallest;
        }

        current_string = static_cast<char>(node->val + 97) + current_string;

        if (node->left) {
            dfs(node->left, current_string);
        }

        if (node->right) {
            dfs(node->right, current_string);
        }

        if (!node->left && !node->right) {
            if (smallest.size() == 0 ||
                std::lexicographical_compare(
                    current_string.begin(), current_string.end(),
                    smallest.begin(), smallest.end())) {
                smallest = current_string;
            }
        }

        return smallest;
    }

 public:
    std::string smallest;
    std::string smallestFromLeaf(TreeNode* root) { return dfs(root); }
};
