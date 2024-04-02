#include <string>
#include <vector>

class Solution {
 public:
    std::vector<std::string> summaryRanges(const std::vector<int>& nums) {
        std::vector<std::string> result;

        int i = 0;
        while (i < nums.size()) {
            int begin;
            int end;
            begin = nums[i];
            while ((i + 1) < nums.size() && nums[i + 1] == (nums[i] + 1)) {
                ++i;
            }
            end = nums[i];
            std::string value = std::to_string(begin);
            if (begin != end) {
                value.append("->");
                value.append(std::to_string(end));
            }
            result.push_back(value);
            ++i;
        }
        return result;
    }
};
