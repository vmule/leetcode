#include <unordered_map>

class Solution {
 public:
    int maxSubarrayLength(const std::vector<int>& nums, int k) {
        int result = 0;
        int left = 0;
        int size = 0;

        std::unordered_map<int, int> counts;

        for (auto num : nums) {
            ++counts[num];
            ++size;

            while (counts[num] > k) {
                int l_num = nums[left];
                --counts[l_num];
                --size;
                ++left;
            }
            result = std::max(result, size);
        }
        return result;
    }
};
