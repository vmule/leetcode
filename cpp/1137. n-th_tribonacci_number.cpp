class Solution {
public:
    int tribonacci(int n) {

        if (n < 1) {
            return 0;
        }

        int fibs[] = {0,0,1};

        --n;
        while (n > 0) {
            int fibs_n = fibs[0] + fibs[1] + fibs[2];
            fibs[0] = fibs[1];
            fibs[1] = fibs[2];
            fibs[2] = fibs_n;
            --n;
        }
    return fibs[2];
    }
};
