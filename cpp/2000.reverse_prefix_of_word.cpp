class Solution {
public:
    std::string reversePrefix(std::string word, char ch) {
        int left = 0;
        int right = 0;

        while (word[right] != ch) {
            if (right == word.size()) {
                return word;
            }
            ++right;
        }

        while (left < right) {
            std::swap(word[left], word[right]);
            --right;
            ++left;
        }
    return word;
    }
};
