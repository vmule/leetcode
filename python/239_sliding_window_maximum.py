from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # use queue so we can pop from beginning efficiently
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            # pop smoller values than values at index r
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                index = q[0]
                res.append(nums[index])
                l += 1
            r += 1
        return res
