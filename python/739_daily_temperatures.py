from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []  # [temp, index]

        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                t, i = stack.pop()
                results[i] = index - i
            stack.append([val, index])
        return results
