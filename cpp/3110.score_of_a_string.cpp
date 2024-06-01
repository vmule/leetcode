#include <string>

class Solution {
 public:
    int scoreOfString(std::string s) {
        int i = 1;
        int result = 0;

        while (i < s.size()) {
            result +=
                std::abs(static_cast<int>(s[i - 1]) - static_cast<int>(s[i]));
            ++i;
        }
        return result;
    }
};
