from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        https://leetcode.com/problems/merge-sorted-array
        """

        i = m
        _ = n

        for element in nums2:
            nums1[i] = element
            i = i + 1

        nums1.sort()
        return nums1
