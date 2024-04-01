#include <string>
#include <unordered_map>

class Solution {
 public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> mappings = {
            {'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}};

        int size = s.size();
        int i = size - 1;
        int result = 0;

        while (i >= 0) {
            if (i < size - 1 && mappings[s[i]] < mappings[s[i + 1]]) {
                result -= mappings[s[i]];
            } else {
                result += mappings[s[i]];
            }
            --i;
        }
        return result;
    }
};
