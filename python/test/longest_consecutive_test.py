#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from longest_consecutive import Solution  # noqa: E402


def main(nums: List[int]) -> int:
    result = Solution().longestConsecutive(nums)

    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = main(nums)
        self.assertEqual(result, 9)

    def test_two(self):
        nums = [100, 4, 200, 1, 3, 2]
        result = main(nums)
        self.assertEqual(result, 4)

    def test_three(self):
        nums = [0, 0]
        result = main(nums)
        self.assertEqual(result, 1)

    def test_four(self):
        nums = []
        result = main(nums)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
