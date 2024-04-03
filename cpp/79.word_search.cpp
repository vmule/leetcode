#include <string>
#include <vector>

class Solution {
 public:
    bool exist(std::vector<std::vector<char>>& board, const std::string word) {
        for (int r = 0; r < board.size(); ++r) {
            for (int c = 0; c < board[0].size(); ++c) {
                if (dfs(board, word, r, c, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

 private:
    bool dfs(std::vector<std::vector<char>>& board, const std::string& word,
             int r, int c, int i) {
        if (i == word.size()) {
            return true;
        }

        if (r < 0 || c < 0 || r >= board.size() || c >= board[0].size() ||
            word[i] != board[r][c]) {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#';

        if (dfs(board, word, r + 1, c, i + 1) ||
            dfs(board, word, r - 1, c, i + 1) ||
            dfs(board, word, r, c + 1, i + 1) ||
            dfs(board, word, r, c - 1, i + 1)) {
            return true;
        }

        board[r][c] = temp;
        return false;
    }
};
