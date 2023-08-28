#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from remove_element import Solution  # noqa: E402


def main(nums: List[int], val: int) -> int:
    result = Solution().removeElement(nums, val)
    return result


class test_sum(unittest.TestCase):
    def test_one(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        returned_value = main(nums, val)
        self.assertEqual(returned_value, 5)

    def test_two(self):
        nums = [3, 2, 2, 3]
        val = 2
        returned_value = main(nums, val)
        self.assertEqual(returned_value, 2)

    def test_three(self):
        nums = [3]
        val = 1
        returned_value = main(nums, val)
        self.assertEqual(returned_value, 1)


if __name__ == "__main__":
    unittest.main()
