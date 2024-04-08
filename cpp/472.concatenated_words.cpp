#include <string>
#include <unordered_set>
#include <vector>

class Solution {
 public:
    std::unordered_map<std::string, bool> cache{};
    std::unordered_set<std::string> u_words{};

    bool dfs(const std::string& word) {
#if __cplusplus >= 202002L
        if (cache.contains(word)) {
#else
        if (cache.find(word) != cache.end()) {
#endif
            return cache[word];
        }

        for (int i = 1; i < word.size(); ++i) {
            std::string prefix = word.substr(0, i);
            std::string suffix = word.substr(i, word.size());

#if __cplusplus >= 202002L
            // C++20 (and later) code
            if (u_words.contains(prefix) && u_words.contains(suffix) ||
                u_words.contains(prefix) && dfs(suffix)) {
                cache[word] = true;
#else
            if (u_words.find(prefix) != u_words.end() &&
                    u_words.find(suffix) != u_words.end() ||
                u_words.find(suffix) != u_words.end() && dfs(suffix)) {
#endif
                cache[word] = true;
                return true;
            }
        }
        cache[word] = false;
        return false;
    }

    std::vector<std::string> findAllConcatenatedWordsInADict(
        const std::vector<std::string>& words) {
        auto result = std::vector<std::string>{};

        for (auto& word : words) {
            u_words.insert(word);
        }

        for (auto& word : words) {
            if (dfs(word)) {
                result.push_back(word);
            }
        }
        return result;
    }
};
