#include <string>
#include <vector>

class Solution {
 public:
    int longestIdealString(std::string s, int k) {
        auto dp = std::vector(26, 0);

        for (auto ch : s) {
            int current = ch - 'a';
            int longest = 1;
            for (int i = 0; i < 26; ++i) {
                if (std::abs(current - i) <= k) {
                    longest = std::max(longest, 1 + dp[i]);
                }
            }
            dp[current] = std::max(dp[current], longest);
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};
