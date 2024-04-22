#include <queue>
#include <string>
#include <unordered_set>

class Solution {
 private:
    std::vector<std::string> findChildren(std::string& combo) {
        auto combos = std::vector<std::string>{};

        for (int i = 0; i < 4; ++i) {
            auto tmp = combo[i];

            // Increase the i-th digit by 1.
            if (combo[i] == '9') {
                combo[i] = '0';
            } else {
                combo[i] = ++combo[i];
            }
            combos.push_back(combo);
            combo[i] = tmp;

            // Decrease the i-th digit by 1.
            if (combo[i] == '0') {
                combo[i] = '9';
            } else {
                combo[i] = --combo[i];
            }
            combos.push_back(combo);
            combo[i] = tmp;
        }
        return combos;
    }

 public:
    int openLock(const std::vector<const std::string>& deadends,
                 const std::string target) {
        std::string initial = "0000";

        if (std::find(deadends.begin(), deadends.end(), initial) !=
            deadends.end()) {
            return -1;
        }

        auto q = std::queue<std::pair<std::string, int>>{};
        auto visited = std::unordered_set<std::string>{};

        for (auto& deadend : deadends) {
            visited.insert(deadend);
        }

        q.push({initial, 0});

        while (!q.empty()) {
            auto combo = q.front().first;
            auto turns = q.front().second;
            q.pop();

            if (combo == target) {
                return turns;
            }
            auto children = findChildren(combo);
            for (auto child : children) {
                if (visited.find(child) == visited.end()) {
                    q.push({child, turns + 1});
                    visited.insert(child);
                }
            }
        }
        return -1;
    }
};
