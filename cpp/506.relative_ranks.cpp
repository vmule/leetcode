#include <map>
#include <string>
#include <vector>

class Solution {
 public:
    std::vector<std::string> findRelativeRanks(const std::vector<int>& score) {
        auto result = std::vector<std::string>(score.size(), "");
        auto score_map = std::map<int, int, std::greater<int>>{};
        auto placements = std::vector<std::string>{"Gold Medal", "Silver Medal",
                                                   "Bronze Medal"};

        int i = 0;
        for (auto s : score) {
            score_map[s] = i;
            ++i;
        }

        i = 0;
        for (auto element : score_map) {
            if (i < 3) {
                result[element.second] = placements[i];
            } else {
                result[element.second] = std::to_string(i + 1);
            }
            ++i;
        }
        return result;
    }
};
