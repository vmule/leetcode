#include <string>

class Solution {
 public:
    static bool compare(std::string a, std::string b) {
        return (a + b) > (b + a);
    }

    // slower and used more memory, but good exercise.
    std::string largestNumber(std::vector<int>& arr) {
        std::vector<std::string> string_arr;

        for (auto num : arr) {
            string_arr.push_back(std::to_string(num));
        }

        std::sort(string_arr.begin(), string_arr.end(), compare);

        std::string ans = "";
        for (auto num : string_arr) {
            ans += num;
        }

        if (ans[0] == '0') {
            return "0";
        }
        return ans;
    }
};

// class Solution {
//  public:
//     static bool compare(int a, int b) {
//         return std::to_string(a) + std::to_string(b) >
//                std::to_string(b) + std::to_string(a);
//     }
//
//     std::string largestNumber(std::vector<int>& arr) {
//         std::sort(arr.begin(), arr.end(), compare);
//
//         std::string ans = "";
//         for (std::uint32_t i = 0; i < arr.size(); ++i) {
//             ans += std::to_string(arr[i]);
//         }
//
//         if (ans[0] == '0') {
//             return "0";
//         }
//         return ans;
//     }
// };
