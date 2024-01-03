#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from three_sum import Solution  # noqa: E402


def main(nums: List[int]) -> List[List[int]]:
    result = Solution().threeSum(nums)

    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = main(nums)
        self.assertEqual(result, [])

    def test_two(self):
        nums = [-100, 4, 200, 1, 3, -100]
        result = main(nums)
        self.assertEqual(result, [[-100, -100, 200]])

    def test_three(self):
        nums = [0, 0, 0]
        result = main(nums)
        self.assertEqual(result, [[0, 0, 0]])

    def test_four(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = main(nums)
        self.assertEqual(result, [[-1, -1, 2], [-1, 0, 1]])


if __name__ == "__main__":
    unittest.main()
