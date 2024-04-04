#include <string>
class Solution {
 public:
    int maxDepth(std::string s) {
        int count = 0;
        int result = 0;

        for (auto ch : s) {
            if (ch == '(') {
                ++count;
            } else if (ch == ')') {
                --count;
            }
            result = std::max(count, result);
        }
        return result;
    }
};
