#include <cstdint>
#include <vector>

class Solution {
 public:
    std::uint32_t firstMissingPositive(std::vector<int>& nums) {
        std::uint32_t size = nums.size();

        for (std::uint32_t i = 0U; i < size; ++i) {
            while (nums[i] >= 1 && nums[i] <= size &&
                   nums[nums[i] - 1] != nums[i]) {
                std::swap(nums[nums[i] - 1], nums[i]);
            }
        }

        for (std::uint32_t i = 0U; i < size; ++i) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        return size + 1;
    }
};
