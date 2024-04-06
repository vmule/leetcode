#include <string>
#include <vector>

class Solution {
 public:
    std::string minRemoveToMakeValid(std::string s) {
        std::string result;
        std::vector<int> _stack;

        for (std::int64_t i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                _stack.push_back(i);
            } else if (s[i] == ')') {
                if (!_stack.empty()) {
                    _stack.pop_back();
                } else {
                    s[i] = '#';
                }
            }
        }

        while (!_stack.empty()) {
            int e = _stack.back();
            _stack.pop_back();
            s[e] = '#';
        }

        for (auto ch : s) {
            if (ch != '#') {
                result.push_back(ch);
            }
        }
        return result;
    }
};
