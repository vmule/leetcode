from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        stack = []

        # create list of pair, position and speed for each car
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        # sort in reverse, based on position
        pos_speed.sort(reverse=True)

        for element in pos_speed:
            time = (target - element[0]) / element[1]
            stack.append(time)
            # if we have at least two elements in the stack and
            # the top element of the stack is smaller than the one below pop
            # [1, 4, 3] means that car will arrive at 3 will catch up with car arriving at 4
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
