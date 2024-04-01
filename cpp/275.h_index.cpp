#include <vector>

class Solution {
 public:
    int hIndex(vector<int>& citations) {
        int size = citations.size();
        int result = 0;

        int low = 0;
        int high = size - 1;
        int mid;

        while (low <= high) {
            mid = low + ((high - low) / 2);
            if (citations[mid] == (size - mid)) {
                return (size - mid);
            } else if (citations[mid] > (size - mid)) {
                high = --mid;
            } else {
                low = ++mid;
            }
        }
        return (size - low);
    }
};
