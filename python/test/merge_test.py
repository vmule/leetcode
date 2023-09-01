#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from merge import Solution  # noqa: E402


def main(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    result = Solution().merge(nums1, m, nums2, n)
    return result


class test_sum(unittest.TestCase):
    def test_one(self):
        nums1 = [1, 2, 2, 3, 4, 0]
        m = 5
        nums2 = [7]
        n = 1
        returned_value = main(nums1, m, nums2, n)
        self.assertEqual(returned_value, [1, 2, 2, 3, 4, 7])

    def test_two(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [7, 8, 9]
        n = 3
        returned_value = main(nums1, m, nums2, n)
        self.assertEqual(returned_value, [1, 2, 3, 7, 8, 9])

    def test_three(self):
        nums1 = [0]
        m = 0
        nums2 = [7]
        n = 1
        returned_value = main(nums1, m, nums2, n)
        self.assertEqual(returned_value, [7])


if __name__ == "__main__":
    unittest.main()
