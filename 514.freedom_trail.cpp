#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int inf = std::numeric_limits<int>::max();
        auto dp = std::vector<int>(ring.size(), 0);

        for (int k = key.size() -1; k >= 0; --k){
            auto next_dp = std::vector<int>(ring.size(), inf);
            for (int r = 0; r < ring.size(); ++r) {
                for (int i = 0; i < ring.size(); ++i) {
                    if (ring[i] == key[k]) {
                        int min_dist = std::min(
                            static_cast<int>(std::abs(r - i)),
                            static_cast<int>((ring.size() - std::abs(r - i)))
                        );
                        next_dp[r] = std::min(
                            static_cast<int>(next_dp[r]),
                            static_cast<int>((min_dist + 1 + dp[i]))
                        );
                    }
                }
            }
            dp = next_dp;
        }
        return dp[0];
    }
};
