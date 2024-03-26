#include <string>

class Solution {
 public:
    static bool compare(int a, int b) {
        return std::to_string(a) + std::to_string(b) >
               std::to_string(b) + std::to_string(a);
    }

    std::string largestNumber(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end(), compare);

        std::string ans = "";
        for (std::uint32_t i = 0; i < arr.size(); ++i) {
            ans += std::to_string(arr[i]);
        }

        if (ans[0] == '0') {
            return "0";
        }
        return ans;
    }
};
