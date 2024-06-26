#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from majority_element import Solution  # noqa: E402


def main(nums: List[int]) -> int:
    result = Solution().majorityElement(nums)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4]
        returned_value = main(nums)
        self.assertEqual(returned_value, 4)

    def test_two(self):
        nums = [1, 1, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, 1)

    def test_three(self):
        nums = [3]
        returned_value = main(nums)
        self.assertEqual(returned_value, 3)

    def test_four(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        returned_value = main(nums)
        self.assertEqual(returned_value, 0)


if __name__ == "__main__":
    unittest.main()
