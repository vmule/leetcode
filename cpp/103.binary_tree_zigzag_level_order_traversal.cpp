#include <queue>
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

class Solution {
 public:
    std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
        auto result = std::vector<std::vector<int>>{};
        auto q = std::queue<TreeNode*>{};

        if (!root) {
            return result;
        }

        bool zigzag = false;
        q.push(root);
        while (!q.empty()) {
            int len = q.size();
            auto level = std::vector<int>{};

            for (int i = 0; i < len; ++i) {
                int value = q.front()->val;
                level.push_back(value);

                if (q.front()->left) {
                    q.push(q.front()->left);
                }
                if (q.front()->right) {
                    q.push(q.front()->right);
                }
                q.pop();
            }
            if (zigzag) {
                std::reverse(level.begin(), level.end());
            }
            zigzag = !zigzag;
            result.push_back(level);
        }
        return result;
    }
};
