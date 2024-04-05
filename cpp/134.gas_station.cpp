#include <numeric>
#include <vector>

class Solution {
 public:
    int canCompleteCircuit(const std::vector<int>& gas,
                           const std::vector<int>& cost) {
        auto sum_gas = std::reduce(gas.begin(), gas.end());
        auto sum_cost = std::reduce(cost.begin(), cost.end());

        if (sum_cost > sum_gas) {
            return -1;
        }

        int total = 0;
        int diff = 0;
        int result = 0;
        for (int i = 0; i < gas.size(); ++i) {
            diff = gas[i] - cost[i];
            total += diff;
            if (total < 0) {
                total = 0;
                result = i + 1;
            }
        }
        return result;
    }
};
