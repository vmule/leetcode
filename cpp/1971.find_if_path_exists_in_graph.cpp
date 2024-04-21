#include <vector>

class Solution {
 private:
    bool dfs(int current, int destination) {
        if (current == destination) {
            return true;
        }

        visited[current] = true;

        for (auto& cur : adj_list[current]) {
            if (visited[cur] == false) {
                if (dfs(cur, destination)) {
                    return true;
                }
            }
        }
        return false;
    }

 public:
    std::vector<std::vector<int>> adj_list;
    std::vector<bool> visited;
    bool validPath(int n, vector<vector<int>>& edges, int source,
                   int destination) {
        adj_list.resize(n);
        visited.assign(n, false);
        int i = 0;
        for (auto& e : edges) {
            int a = e[0];
            int b = e[1];
            adj_list[e[0]].push_back(e[1]);
            adj_list[e[1]].push_back(e[0]);
        }
        return dfs(source, destination);
    }
};
