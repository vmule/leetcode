#include <cmath>
#include <vector>

class Solution {
 public:
    std::vector<int> findDuplicates(std::vector<int>& nums) {
        std::vector<int> result;

        for (auto num : nums) {
            // [2, 5, 2, 1, 1, 4]
            // idx = 2 - 1 = 1
            // nums[1] = 5 * -1 = -5
            int idx = std::abs(num) - 1;
            if (nums[idx] < 0) {
                result.push_back(idx + 1);
            }
            nums[idx] *= -1;
        }
        return result;
    }
};
