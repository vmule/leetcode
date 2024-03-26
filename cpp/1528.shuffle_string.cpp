#include <string>
#include <vector>
class Solution {
 public:
    std::string restoreString(const std::string s,
                              const std::vector<int>& indices) {
        std::string result(indices.size(), 'a');
        for (auto i = 0; i < indices.size(); ++i) {
            result[indices[i]] = s[i];
        }
        return result;
    }
};
