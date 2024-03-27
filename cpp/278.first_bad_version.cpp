// The API isBadVersion is defined for you.
bool isBadVersion(int version);

class Solution {
 public:
    // TODO: implement with binary search
    int firstBadVersion(int n) {
        int i = 0;
        int result = 0;
        for (int i = 0; i <= n; ++i) {
            if (isBadVersion(i)) {
                result = i;
                break;
            }
        }
        return result;
    }
};
