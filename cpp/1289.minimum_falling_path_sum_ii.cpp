#include <limits>
#include <vector>

class Solution {
 public:
    int minFallingPathSum(const std::vector<std::vector<int>>& grid) {
        int n = grid.size();

        if (n < 2) {
            return grid[0][0];
        }
        int inf = std::numeric_limits<int>::max();

        auto dp = grid[0];
        for (int r = 1; r < n; ++r) {
            auto next_dp = std::vector(n, inf);
            for (int cur_col = 0; cur_col < n; ++cur_col) {
                for (int prev_col = 0; prev_col < n; ++prev_col) {
                    if (cur_col != prev_col) {
                        next_dp[cur_col] = std::min(
                            next_dp[cur_col], grid[r][cur_col] + dp[prev_col]);
                    }
                }
            }
            dp = next_dp;
        }
        return *std::min_element(dp.begin(), dp.end());
    }
};
