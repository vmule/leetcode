#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
 public:
    int findMaxK(const std::vector<int>& nums) {
        auto uniq = std::unordered_set<int>{};
        int result = -1;

        for (auto num : nums) {
            int matching_num = -1 * num;
            if (uniq.contains(matching_num)) {
                result = std::max(result, std::abs(num));
            } else {
                uniq.insert(num);
            }
        }
        return result;
    }
};
