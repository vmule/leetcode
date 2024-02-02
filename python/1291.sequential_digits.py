from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        q = deque(range(1, 10))

        while q:
            n = q.popleft()
            if n > high:
                continue
            if n >= low and n <= high:
                result.append(n)

            # 123 % 10 = 3
            # 123 * 1 = 1230
            # 1230 + 4 = 1234
            ones = n % 10
            if ones < 9:
                q.append(n * 10 + (ones + 1))

        return result
