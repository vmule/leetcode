#include <algorithm>
#include <string>
#include <vector>

class Solution {
 public:
    std::vector<std::string> fullJustify(const std::vector<std::string>& words,
                                         int maxWidth) {
        auto result = std::vector<std::string>{};
        auto line = std::vector<std::string>{};

        int i = 0;
        int length = 0;
        int line_size = 0;
        std::string line_string;

        if (maxWidth < 2) {
            return words;
        }

        while (i < words.size()) {
            line_size = line.size();
            if ((length + line_size + words[i].size()) > maxWidth) {
                int extra_space = maxWidth - length;
                int spaces = extra_space / std::max(1, (line_size - 1));
                int remainder = extra_space % std::max(1, (line_size - 1));

                for (int j = 0; j < std::max(1, line_size - 1); ++j) {
                    int counter = spaces;
                    while (counter > 0) {
                        line[j].append(" ");
                        --counter;
                    }
                    if (remainder > 0) {
                        line[j].append(" ");
                        --remainder;
                    }
                }

                for (auto e : line) {
                    line_string.append(e);
                }

                result.push_back(line_string);
                length = 0;
                line.clear();
                line_string = "";
                continue;
            }

            line.push_back(words[i]);
            length += words[i].size();
            ++i;
        }

        // last line
        line_size = line.size();
        for (int j = 0; j < line_size - 1; ++j) {
            line[j].append(" ");
        }

        for (auto e : line) {
            line_string.append(e);
        }

        int trailing_spaces = maxWidth - line_string.size();
        while (trailing_spaces > 0) {
            line_string.append(" ");
            --trailing_spaces;
        }
        result.push_back(line_string);
        return result;
    }
};
