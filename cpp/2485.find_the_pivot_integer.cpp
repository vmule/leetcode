#include <cmath>

class Solution {
 public:
    int pivotInteger(const int& n) {
        int sum = n * (n + 1) / 2;
        double a = std::sqrt(sum);

        if (std::fmod(a, 1) == 0) {
            return static_cast<int>(a);
        } else {
            return -1;
        }
    }
};
