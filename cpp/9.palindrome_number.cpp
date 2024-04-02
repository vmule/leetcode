#include <string>

class Solution {
 public:
    bool isPalindrome(int x) {
        std::string xS = std::to_string(x);
        std::string xS_r;
        for (int i = xS.size() - 1; i >= 0; --i) {
            xS_r.push_back(xS[i]);
        }

        if (xS == xS_r) {
            return true;
        }
        return false;
    }
};
