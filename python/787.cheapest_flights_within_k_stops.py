from collections import defaultdict
from queue import Queue
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        dist = [float("inf")] * n
        dist[src] = 0

        q = Queue()
        q.put((src, 0))
        stops = 0

        while q and stops <= k:
            size = q.qsize()
            for i in range(size):
                node, distance = q.get()

                if node not in adj:
                    continue
                for neighbour, price in adj[node]:
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.put((neighbour, dist[neighbour]))
            stops += 1

        if dist[dst] != float("inf"):
            return dist[dst]
        return -1
