import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        # available rooms
        available = [i for i in range(n)]
        # (end_time, room_number)
        used = []
        # count[n] = meetings schedule
        count = [0] * n

        for start, end in meetings:
            # finsh meetings
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # no room is available
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            # a room is available
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))
