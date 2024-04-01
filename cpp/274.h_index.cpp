#include <vector>

class Solution {
 public:
    int hIndex(std::vector<int>& citations) {
        std::sort(citations.begin(), citations.end());
        int size = citations.size();
        int result = 0;

        int i = 0;
        for (auto cit : citations) {
            if (citations[i] >= (size - i)) {
                return (size - i);
            }
            ++i;
        }
        return 0;
    }
};
