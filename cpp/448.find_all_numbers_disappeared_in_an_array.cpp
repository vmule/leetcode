#include <vector>

class Solution {
 public:
    std::vector<int> findDisappearedNumbers(std::vector<int>& nums) {
        std::vector<int> result;

        for (auto num : nums) {
            // since each (number -1) in the array corresponds to an index
            // we keep flipping numbers to negative for each idx = num - 1
            int i = abs(num) - 1;
            nums[i] = -1 * abs(nums[i]);
        }

        int i = 0;
        for (auto num : nums) {
            if (num > 0) {
                result.push_back(i + 1);
            }
            ++i;
        }
        return result;
    }
};
