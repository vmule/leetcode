class Solution {
 public:
    std::vector<int> replaceElements(std::vector<int>& arr) {
        int n = arr.size() - 1;
        int rightMax = -1;

        for (int i = n; i >= 0; --i) {
            int newMax = std::max(rightMax, arr[i]);
            arr[i] = rightMax;
            rightMax = newMax;
        }
        return arr;
    }
};
