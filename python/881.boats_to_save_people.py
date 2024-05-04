from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
