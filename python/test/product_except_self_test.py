#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from product_except_self import Solution  # noqa: E402


def main(nums: List[int]) -> List[int]:
    result = Solution().productExceptSelf(nums)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3, 4]
        returned_value = main(nums)
        self.assertEqual(returned_value, [24, 12, 8, 6])

    def test_two(self):
        nums = [-1, 1, 0, -3, 3]
        returned_value = main(nums)
        self.assertEqual(returned_value, [0, 0, 9, 0, 0])

    def test_three(self):
        nums = [-1, 1, 33, -3, 3]
        returned_value = main(nums)
        self.assertEqual(returned_value, [-297, 297, 9, -99, 99])

    def test_four(self):
        nums = [0, 0]
        returned_value = main(nums)
        self.assertEqual(returned_value, [0, 0])


if __name__ == "__main__":
    unittest.main()
