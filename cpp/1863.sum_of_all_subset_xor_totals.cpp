class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int result = 0;
        for (auto& n : nums) {
            result = result | n;
        }
        return result * pow(2, (nums.size() - 1));
    }
};
