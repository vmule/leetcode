#include <vector>

class Solution {
 private:
    void dfs(const int r, const int c, int& r2, int& c2,
             std::vector<std::vector<int>>& land) {
        const int rows = land.size();
        const int cols = land[0].size();

        land[r][c] = 2;
        int dir_r[4] = {-1, 1, 0, 0};
        int dir_c[4] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nr = dir_r[i] + r;
            int nc = dir_c[i] + c;

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                land[nr][nc] == 1) {
                r2 = std::max(r2, nr);
                c2 = std::max(c2, nc);
                dfs(nr, nc, r2, c2, land);
            }
        }
    }

 public:
    std::vector<std::vector<int>> result{};

    std::vector<std::vector<int>> findFarmland(
        std::vector<std::vector<int>>& land) {
        const int rows = land.size();
        const int cols = land[0].size();

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (land[i][j] == 1) {
                    int r2 = i;
                    int c2 = j;
                    dfs(i, j, r2, c2, land);
                    result.push_back({i, j, r2, c2});
                }
            }
        }
        return result;
    }
};
