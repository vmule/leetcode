class Solution {
 public:
    std::vector<int> getConcatenation(std::vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            nums.push_back(nums[i]);
        }
        return nums;

        /*
         * std::vector<int> ans;
         * ans.reserve(ans.size() + nums.size() + nums.size());
         * std::move(nums.begin(), nums.end(), std::inserter(ans,
         * ans.end())); std::move(nums.begin(), nums.end(), std::inserter(ans,
         * ans.end())); return ans;
         */
    }
};
