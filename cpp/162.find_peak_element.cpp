#include <vector>

class Solution {
 public:
    int findPeakElement(std::vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        if (right == 0) {
            return 0;
        }

        while (left <= right) {
            int mid = left + ((right - left) / 2);

            if (mid > 0 && nums[mid - 1] > nums[mid]) {
                right = mid - 1;
            } else if (mid < nums.size() - 1 && nums[mid + 1] > nums[mid]) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return 0;
    }
};
