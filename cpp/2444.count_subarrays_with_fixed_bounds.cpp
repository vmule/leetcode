#include <algorithm>

class Solution {
 public:
    long long countSubarrays(std::vector<int>& nums, int minK, int maxK) {
        long long result = 0;
        int bad_i = -1;
        int min_i = -1;
        int max_i = -1;

        int i = 0;
        for (int num : nums) {
            if (num < minK || num > maxK) {
                bad_i = i;
            }

            if (num == minK) {
                min_i = i;
            }

            if (num == maxK) {
                max_i = i;
            }
            result += std::max(0, (std::min(min_i, max_i) - bad_i));
            ++i;
        }

        return result;
    }
};
