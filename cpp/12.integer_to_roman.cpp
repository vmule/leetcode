#include <string>

class Solution {
 public:
    std::string intToRoman(int num) {
        std::string ones[] = {"",  "I",  "II",  "III",  "IV",
                              "V", "VI", "VII", "VIII", "IX"};
        std::string tens[] = {"",  "X",  "XX",  "XXX",  "XL",
                              "L", "LX", "LXX", "LXXX", "XC"};
        std::string hundreds[] = {"",  "C",  "CC",  "CCC",  "CD",
                                  "D", "DC", "DCC", "DCCC", "CM"};
        std::string thousands[] = {"", "M", "MM", "MMM"};

        return thousands[num / 1000] + hundreds[(num % 1000) / 100] +
               tens[(num % 100) / 10] + ones[num % 10];
    }
};
