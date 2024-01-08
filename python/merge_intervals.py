from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        # append first value of intervals, since we sorted the list
        res.append(intervals[0])

        # start from index 1
        i = 1

        # iterate and compare that the current interval start is lesser than the previous interval end
        # pick the max between the current interval end and previous interval end
        while i <= len(intervals) - 1:
            if intervals[i][0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], intervals[i][-1])
            # if current interval start is greater than previous interval end just append it
            else:
                res.append(intervals[i])
            i += 1

        return res
