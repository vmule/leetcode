from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort list of intervals
        intervals.sort()

        # save initial length of the intervals list
        i_length = len(intervals)

        # start from second element of the list
        i = 1

        while i < len(intervals):
            # compare end of previous interval if it's greater than start of current interval
            if intervals[i - 1][1] > intervals[i][0]:
                # pop interval than ends after
                if intervals[i - 1][1] > intervals[i][1]:
                    intervals.pop(i - 1)
                else:
                    intervals.pop(i)
                continue
            else:
                # increase i only if we didn't pop anything
                i = i + 1
        # return initial length minus current length
        return i_length - len(intervals)
