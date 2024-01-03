#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from find_duplicate import Solution  # noqa: E402


def main(nums: List[int]) -> int:
    result = Solution().findDuplicate(nums)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [3, 1, 3, 4, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, 3)

    def test_two(self):
        nums = [1, 2, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, 2)

    def test_three(self):
        nums = [1, 3, 4, 2, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, 2)


if __name__ == "__main__":
    unittest.main()
