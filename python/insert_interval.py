from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # check if new intervals ends before first interval in intervals
            if newInterval[-1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # check if new interval start after interval at index i
            elif newInterval[0] > intervals[i][-1]:
                res.append(intervals[i])

            # intervals overlap get min, max of start, end values
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[-1], intervals[i][-1]),
                ]
        # make sure we append last interval
        res.append(newInterval)
        return res
