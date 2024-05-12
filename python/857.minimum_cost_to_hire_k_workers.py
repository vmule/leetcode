import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        result = float("inf")
        pairs = []  # ratio, quality

        for i in range(len(quality)):
            pair = ((wage[i] / quality[i]), quality[i])
            pairs.append(pair)
        pairs.sort(key=lambda p: p[0])

        max_heap = []
        total_quality = 0

        for rate, qual in pairs:
            heapq.heappush(max_heap, -1 * qual)
            total_quality += qual

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                result = min(result, total_quality * rate)
        return result
