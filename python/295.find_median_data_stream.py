import heapq


class MedianFinder:
    """https://leetcode.com/problems/find-median-from-data-stream"""

    def __init__(self):
        # Using two heaps, small and large
        # small is a maxHeap, large is minHeap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Add by default to small heap
        heapq.heappush(self.small, -1 * num)

        # make sure num small is < num in large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # make sure len small is similar to len large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # make sure len large is similar to len small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
