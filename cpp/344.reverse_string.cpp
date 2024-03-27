#include <vector>

class Solution {
 public:
    void reverseString(std::vector<char>& s) {
        int left = 0;
        int right = s.size() - 1;

        while (left <= right) {
            // swap(s[left], s[right]);
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            ++left;
            --right;
        }
    }
};
