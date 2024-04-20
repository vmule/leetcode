#include <stack>
#include <string>

class Solution {
 public:
    std::string decodeString(std::string st) {
        std::stack<std::string> s;
        std::stack<int> nums;
        std::string result;

        int len = st.length();
        for (int i = 0; i < len; ++i) {
            if (isdigit(st[i])) {
                int count = 0;
                while (i < len && isdigit(st[i])) {
                    count = (count * 10) + (st[i] - '0');
                    ++i;
                }
                --i;
                nums.push(count);
            } else if (st[i] == '[') {
                s.push(result);
                result = "";
            } else if (st[i] == ']') {
                int count = nums.top();
                nums.pop();
                std::string tmp = s.top();
                s.pop();
                while (count > 0) {
                    tmp += result;
                    --count;
                }
                result = tmp;
            } else {
                result += st[i];
            }
        }
        return result;
    }
};
