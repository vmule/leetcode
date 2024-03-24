class Solution {
 public:
    int removeElement(std::vector<int>& nums, int val) {
        auto k = 0;
        auto i = 0;
        for (auto num : nums) {
            if (num != val) {
                nums[k] = nums[i];
                ++k;
            }
            ++i;
        }
        return k;
    }
};
