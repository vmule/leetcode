#include <vector>

class Solution {
 public:
    int searchInsert(const std::vector<int>& nums, const int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = 0;

        while (left <= right) {
            mid = left + ((right - left) / 2);

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
