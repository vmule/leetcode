#include <deque>
#include <vector>

class Solution {
 public:
    std::vector<int> deckRevealedIncreasing(std::vector<int>& deck) {
        auto result = std::vector<int>{};
        auto q = std::deque<int>{};

        std::sort(deck.begin(), deck.end());
        int i = deck.size() - 1;
        while (i >= 0) {
            q.push_front(deck[i]);
            if (i > 0) {
                int tmp = q.back();
                q.pop_back();
                q.push_front(tmp);
            }
            --i;
        }

        for (auto i : q) {
            result.push_back(i);
        }
        return result;
    }
};
