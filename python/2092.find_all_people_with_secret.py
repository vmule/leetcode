from collections import defaultdict
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:

        secrets = set()
        secrets.add(0)
        secrets.add(firstPerson)

        time_map = defaultdict(list)

        for src, dst, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)
            time_map[time][src].append(dst)
            time_map[time][dst].append(src)

        def dfs(src, adj):
            if src in visited:
                return
            visited.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        for time in sorted(time_map.keys()):
            visited = set()
            for src in time_map[time]:
                if src in secrets:
                    dfs(src, time_map[time])

        return list(secrets)
