#include <queue>
#include <vector>

class Solution {
 private:
    void bfs(int i, int j, std::vector<std::vector<char>>& grid) {
        auto dirs =
            std::vector<std::pair<int, int>>{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        auto q = std::queue<std::pair<int, int>>{};
        const int rows = grid.size();
        const int cols = grid[0].size();

        grid[i][j] = '#';
        auto pair = std::make_pair(i, j);
        q.push(pair);

        while (!q.empty()) {
            auto element = q.front();
            int cur_r = element.first;
            int cur_c = element.second;
            q.pop();

            for (auto dir : dirs) {
                int r = cur_r + dir.first;
                int c = cur_c + dir.second;

                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    if (grid[r][c] == '1') {
                        grid[r][c] = '#';
                        auto pair = std::make_pair(r, c);
                        q.push(pair);
                    }
                }
            }
        }
    }

 public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        int islands = 0;

        if (grid.empty()) {
            return islands;
        }

        int rows = grid.size();
        int cols = grid[0].size();

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == '1') {
                    bfs(i, j, grid);
                    ++islands;
                }
            }
        }
        return islands;
    }
};
