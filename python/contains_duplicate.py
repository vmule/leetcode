from typing import List


class Solution:
    """
    https://leetcode.com/problems/contains-duplicate
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = set()

        for num in nums:
            if num in uniq:
                return True
            else:
                uniq.add(num)
        return False
