#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        std::vector<int> result;

        unsigned i = 0;

        for (auto& num : nums) {
            int diff = target - num;
            if (seen.contains(diff)) {
                result.push_back(seen[diff]);
                result.push_back(i);
                return result;
            }
            else {
                seen[num] = i;
                ++i;
            }
        }
        return {};
    }
};
