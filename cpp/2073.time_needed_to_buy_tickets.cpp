#include <vector>

class Solution {
 public:
    int timeRequiredToBuy(std::vector<int>& tickets, const int k) {
        int n = tickets.size();
        int result = 0;
        while (true) {
            for (int i = 0; i < n; i++) {
                if (tickets[i] >= 1) {
                    ++result;
                    --tickets[i];
                    if (tickets[k] == 0) {
                        return result;
                    }
                }
            }
        }
        return result;
    }
};
