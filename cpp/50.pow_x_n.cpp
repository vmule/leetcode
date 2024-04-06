#include <cmath>
#include <cstdint>

class Solution {
 public:
    double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }

        if (n == 1) {
            return x;
        }

        double result = 1.0;
        int64_t pow = std::abs(n);

        while (pow > 0) {
            if (pow % 2 == 1) {
                result = result * x;
                --pow;
            } else {
                x *= x;
                pow /= 2;
            }
        }

        if (n < 0) {
            return 1.0 / result;
        }

        return result;
    }
};
