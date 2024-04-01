#include <cstdint>
#include <vector>

class Solution {
 public:
    std::int64_t countSubarrays(const std::vector<int>& nums, int k) {
        std::int64_t max_num =
            *std::max_element(std::begin(nums), std::end(nums));
        std::int64_t result = 0;
        auto left = 0;
        auto count = 0;

        auto right = 0;
        for (auto num : nums) {
            if (nums[right] == max_num) {
                ++count;
            }
            while (count >= k) {
                result += (nums.size() - right);
                if (nums[left] == max_num) {
                    --count;
                }
                ++left;
            }
            ++right;
        }
        return result;
    }
};
