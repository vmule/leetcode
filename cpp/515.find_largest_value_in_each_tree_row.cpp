#include <queue>
#include <vector>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};

class Solution {
 public:
    std::vector<int> largestValues(TreeNode* root) {
        std::vector<int> result;

        if (!root) {
            return result;
        }

        std::queue<TreeNode*> q({root});

        while (!q.empty()) {
            int row_max = q.front()->val;
            int len = q.size();
            for (int i = 0; i < len; ++i) {
                TreeNode* node = q.front();
                q.pop();
                row_max = std::max(row_max, node->val);
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            result.push_back(row_max);
        }
        return result;
    }
};
