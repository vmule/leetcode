#include <unordered_set>
#include <vector>

class Solution {
 public:
    int findDuplicate(const std::vector<int>& nums) {
        std::unordered_set<int> uniq;

        for (auto num : nums) {
            if (uniq.find(num) != uniq.end()) {
                return num;
            }
            uniq.insert(num);
        }
        return -1;
    }
};
