#include <sstream>
#include <stack>
#include <string>

class Solution {
 public:
    std::string simplifyPath(std::string path) {
        std::string substring = "";
        std::stringstream ss(path);
        std::stack<std::string> _stack;

        while (getline(ss, substring, '/')) {
            if (substring == "" || substring == ".") {
                continue;
            } else if (substring == "..") {
                if (!_stack.empty()) {
                    _stack.pop();
                }
            } else if (substring != "") {
                _stack.push(substring);
            }
        }

        std::string result = "";

        while (!_stack.empty()) {
            result = "/" + _stack.top() + result;
            _stack.pop();
        }

        if (result.length() == 0) {
            result = "/";
        }
        return result;
    }
};
