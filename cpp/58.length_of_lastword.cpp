#include <sstream>
#include <string>

class Solution {
 public:
    // Alternative solution using stringstream
    // also check strtok()
    int lengthOfLastWordSS(std::string s) {
        std::stringstream ss(s);
        std::string word;
        while (ss >> word) {
            {
            }
        }
        return word.size();
    }

    int lengthOfLastWord(std::string s) {
        int n = s.size() - 1;
        int result = 0;

        for (char ch : s) {
            if (s[n] == ' ' && result > 0) {
                return result;
            }
            if (s[n] != ' ') {
                ++result;
            }
            --n;
        }
        return result;
    }
};
