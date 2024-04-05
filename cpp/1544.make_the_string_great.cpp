#include <string>
#include <vector>

class Solution {
 public:
    std::string makeGood(std::string s) {
        std::vector<char> list;

        for (char ch : s) {
            if (!list.empty() && std::abs(static_cast<int>(list.back()) -
                                          static_cast<int>(ch)) == 32) {
                list.pop_back();
            } else {
                list.push_back(ch);
            }
        }
        std::string result;
        for (char ch : list) {
            result.push_back(ch);
        }
        return result;
    }
};
