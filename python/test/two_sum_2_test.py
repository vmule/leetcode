#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from two_sum_2 import Solution  # noqa: E402


def main(nums: List[int], target: int) -> List[int]:
    result = Solution().twoSum(nums, target)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 1, 2, 3, 17]
        target = 5
        returned_value = main(nums, target)
        self.assertEqual(returned_value, [3, 4])

    def test_two(self):
        nums = [1, 2, 3]
        target = 5
        returned_value = main(nums, target)
        self.assertEqual(returned_value, [2, 3])

    def test_three(self):
        nums = [0, 0, 1]
        target = 0
        returned_value = main(nums, target)
        self.assertEqual(returned_value, [1, 2])

    def test_four(self):
        nums = [3, 4]
        target = 7
        returned_value = main(nums, target)
        self.assertEqual(returned_value, [1, 2])

    def test_five(self):
        nums = [1, 2, 7]
        target = 8
        returned_value = main(nums, target)
        self.assertEqual(returned_value, [1, 3])

    def test_six(self):
        nums = [0, 1, 2, 3, 4]
        target = 1
        returned_value = main(nums, target)
        self.assertEqual(returned_value, [1, 2])


if __name__ == "__main__":
    unittest.main()
