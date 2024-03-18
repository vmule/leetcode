from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        arrows = len(points)

        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1]:
                arrows -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr

        return arrows
