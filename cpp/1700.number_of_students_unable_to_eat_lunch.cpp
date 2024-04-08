#include <queue>
#include <stack>
#include <unordered_map>

class Solution {
 public:
    int countStudents(const std::vector<int>& students,
                      const std::vector<int>& sandwiches) {
        std::unordered_map<int, int> counts;
        int result = students.size();

        for (auto s : students) {
            ++counts[s];
        }

        for (auto s : sandwiches) {
            if (counts[s] > 0) {
                --result;
                --counts[s];
            } else {
                return result;
            }
        }
        return result;

        /*
        std::queue<int> students_q;
        std::stack<int> sandwiches_s;


        for (auto s : students) {
            students_q.push(s);
        }

        for (int i = sandwiches.size() - 1; i >= 0; --i) {
            sandwiches_s.push(sandwiches[i]);
        }

        int count = 0;
        while (!students_q.empty()) {
            if (count == students_q.size()) {
                break;
            }

            if (students_q.front() == sandwiches_s.top()) {
                students_q.pop();
                sandwiches_s.pop();
                count = 0;
            }
            else {
                int e = students_q.front();
                students_q.push(e);
                students_q.pop();
                ++count;
            }
        }
        return students_q.size();
        */
    }
};
