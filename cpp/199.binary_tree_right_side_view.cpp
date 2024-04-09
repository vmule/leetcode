#include <deque>

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
    std::vector<int> rightSideView(TreeNode* root) {
        auto result = std::vector<int>{};

        if (!root) {
            return result;
        }

        auto q = std::deque<TreeNode*>{root};

        while (!q.empty()) {
            TreeNode* rightSide = nullptr;

            auto len = q.size();

            for (auto i = 0; i < len; ++i) {
                auto node = q.front();
                q.pop_front();

                if (node) {
                    rightSide = node;
                    q.push_back(node->left);
                    q.push_back(node->right);
                }
            }

            if (rightSide) {
                result.push_back(rightSide->val);
            }
        }
        return result;
    }
};
