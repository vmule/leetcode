#include <iostream>
#include <unordered_set>
#include <vector>

class Solution {
 public:
    std::vector<int> intersection(const std::vector<int>& nums1,
                                  const std::vector<int>& nums2) {
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> set2(nums2.begin(), nums2.end());

        std::vector<int> result;
        for (const auto& num : set1) {
            if (set2.find(num) != set2.end()) {
                result.push_back(num);
            }
        }
        return result;
    }
};

int main() {
    std::vector<int> one{1, 2, 3, 4, 5, 6, 7};
    std::vector<int> two{4, 5, 6, 7};

    Solution sol;
    std::vector<int> result = sol.intersection(one, two);
    for (auto num : result) {
        std::cout << num << std::endl;
    }

    return 0;
}
