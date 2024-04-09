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
    std::vector<double> averageOfLevels(TreeNode* root) {
        auto q = std::queue<TreeNode*>{};
        auto result = std::vector<double>{};

        q.push(root);
        while (!q.empty()) {
            int len = q.size();
            double sum = 0;

            for (int i = 0; i < len; ++i) {
                int value = q.front()->val;
                sum += value;

                if (q.front()->left) {
                    q.push(q.front()->left);
                }
                if (q.front()->right) {
                    q.push(q.front()->right);
                }
                q.pop();
            }
            result.push_back(sum / len);
        }
        return result;
    }
};
