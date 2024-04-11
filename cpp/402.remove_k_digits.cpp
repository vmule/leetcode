#include <string>

class Solution {
 public:
    std::string removeKdigits(std::string num, int k) {
        auto result = std::string{};

        for (auto n : num) {
            while (!result.empty() && k > 0 && result.back() > n) {
                result.pop_back();
                --k;
            }
            result.push_back(n);
        }

        while (k > 0) {
            result.pop_back();
            --k;
        }

        while (result.front() == '0') {
            result.erase(result.begin() + 0);
        }

        if (result.size() < 1) {
            return "0";
        }

        return result;
    }
};
