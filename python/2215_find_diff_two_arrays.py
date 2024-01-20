from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-the-difference-of-two-arrays
    """

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        one liner
        return [
            list(set(nums1) - set(nums2)),
            list(set(nums2) - set(nums1))
        ]
        """

        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = set1 - set2
        diff2 = set2 - set1

        result = [list(diff1), list(diff2)]

        return result
