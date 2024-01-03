#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from search import Solution  # noqa: E402


def main(nums: List, target: int) -> int:
    result = Solution().search(nums, target)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [3, 4, 5, 1, 2]
        target = 4
        returned_value = main(nums, target)
        self.assertEqual(returned_value, 1)

    def test_two(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        returned_value = main(nums, target)
        self.assertEqual(returned_value, 4)

    def test_three(self):
        nums = [11, 13, 15, 17]
        target = 17
        returned_value = main(nums, target)
        self.assertEqual(returned_value, 3)


if __name__ == "__main__":
    unittest.main()
