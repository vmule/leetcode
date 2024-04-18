#include <unordered_set>
#include <vector>

class Solution {
 public:
    struct pair_hash {
        std::size_t operator()(const std::pair<int, int>& v) const {
            return v.first * 97 + v.second;
        }
    };

    std::unordered_set<std::pair<int, int>, pair_hash> visited{};
    int row_size;
    int col_size;

    int islandPerimeter(const std::vector<std::vector<int>>& grid) {
        row_size = grid.size();
        col_size = grid[0].size();

        for (int i = 0; i < row_size; ++i) {
            for (int j = 0; j < col_size; ++j) {
                if (grid[i][j] == 1) {
                    return dfs(i, j, grid);
                }
            }
        }
        return -1;
    }

 private:
    int dfs(int i, int j, const std::vector<std::vector<int>>& grid) {
        int perimeter = 0;

        if (i < 0 || j < 0) {
            return 1;
        }

        if (i >= row_size || j >= col_size) {
            return 1;
        }

        if (grid[i][j] == 0) {
            return 1;
        }

        auto pair = std::pair<int, int>(i, j);
        if (!visited.empty() && visited.find(pair) != visited.end()) {
            return 0;
        }

        visited.insert(pair);
        perimeter += dfs(i - 1, j, grid);
        perimeter += dfs(i + 1, j, grid);
        perimeter += dfs(i, j - 1, grid);
        perimeter += dfs(i, j + 1, grid);

        return perimeter;
    }
};
