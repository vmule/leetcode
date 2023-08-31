#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from is_monotonic import Solution  # noqa: E402


def main(nums: List[int]) -> bool:
    result = Solution().isMonotonic(nums)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, False)

    def test_two(self):
        nums = [1, 2, 3]
        returned_value = main(nums)
        self.assertEqual(returned_value, True)

    def test_three(self):
        nums = [3, 2, 1]
        returned_value = main(nums)
        self.assertEqual(returned_value, True)

    def test_four(self):
        nums = [3]
        returned_value = main(nums)
        self.assertEqual(returned_value, True)

    def test_five(self):
        nums = [1, 1, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, True)

    def test_six(self):
        nums = [1, 1, 0]
        returned_value = main(nums)
        self.assertEqual(returned_value, True)


if __name__ == "__main__":
    unittest.main()
