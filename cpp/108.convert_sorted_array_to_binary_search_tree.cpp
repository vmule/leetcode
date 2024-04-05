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
    TreeNode* sortedArrayToBST(const std::vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        TreeNode* result = helper(nums, left, right);

        return result;
    }

 private:
    TreeNode* helper(const std::vector<int>& nums, int left, int right) {
        if (left > right) {
            return nullptr;
        }

        int mid = left + ((right - left) / 2);

        TreeNode* root = new TreeNode(nums[mid]);
        root->left = helper(nums, left, mid - 1);
        root->right = helper(nums, mid + 1, right);

        return root;
    }
};
