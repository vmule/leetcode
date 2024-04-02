#include <string>

class Solution {
 public:
    std::string convert(std::string s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        std::string result;
        int increment = 2 * (numRows - 1);

        int row = 0;
        while (row < numRows) {
            int i = row;
            while (i < s.size()) {
                result.push_back(s[i]);
                if (row > 0 && row < (numRows - 1) &&
                    (i + increment - (2 * row)) < s.size()) {
                    int idx = i + increment - (2 * row);
                    result.push_back(s[idx]);
                }
                i += increment;
            }
            ++row;
        }
        return result;
    }
};
