#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from non_decresing_array import Solution  # noqa: E402


def main(nums: List[int]) -> bool:
    result = Solution().checkPossibility(nums)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = main(nums)
        self.assertEqual(result, False)

    def test_two(self):
        nums = [100, 200, 1]
        result = main(nums)
        self.assertEqual(result, True)

    def test_three(self):
        nums = [0]
        result = main(nums)
        self.assertEqual(result, True)

    def test_four(self):
        nums = [4, 2, 1]
        result = main(nums)
        self.assertEqual(result, False)

    def test_five(self):
        nums = [4, 2, 3]
        result = main(nums)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
