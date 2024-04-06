#include <vector>

class Solution {
 public:
    int candy(const std::vector<int>& ratings) {
        std::vector<int> arr(ratings.size(), 1);

        for (int i = 1; i < ratings.size(); ++i) {
            if (ratings[i - 1] < ratings[i]) {
                arr[i] = arr[i - 1] + 1;
            }
        }

        for (int i = ratings.size() - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1]) {
                arr[i] = std::max(arr[i], arr[i + 1] + 1);
            }
        }

        int result = 0;
        for (int num : arr) {
            result += num;
        }
        return result;
    }
};
