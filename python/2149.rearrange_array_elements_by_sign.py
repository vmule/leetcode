from typing import List


class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        for i in range(len(pos)):
            nums[i * 2] = pos[i]
            nums[(i * 2) + 1] = neg[i]

        return nums
