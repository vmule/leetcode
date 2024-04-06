#include <unordered_map>
#include <vector>

class Solution {
 public:
    int singleNumber(const std::vector<int>& nums) {
        // unordered_mapp approach
        // Time: O(n)
        // Memory; O(n)
        if (nums.size() == 1) {
            return nums[0];
        }

        std::unordered_map<int, int> counts;

        for (auto num : nums) {
            ++counts[num];
        }

        int result_map;
        for (auto i = counts.begin(); i != counts.end(); i++) {
            if (i->second == 1) {
                result_map = i->first;
            }
        }

        // xor approach
        // Time: O(n)
        // Memory; O(n)
        int result_xor = 0;
        for (auto num : nums) {
            result_xor ^= num;
        }

        return (result_xor + result_map) / 2;
    }
};
