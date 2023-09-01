#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from rotate import Solution  # noqa: E402


def main(nums: List[int], k: int) -> List[int]:
    result = Solution().rotate(nums, k)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [0, 0, 1, 2, 2, 2, 3, 4]
        k = 3
        returned_value = main(nums, k)
        self.assertEqual(returned_value, [2, 3, 4, 0, 0, 1, 2, 2])

    def test_two(self):
        nums = [1, 1, 2]
        k = 1
        returned_value = main(nums, k)
        self.assertEqual(returned_value, [2, 1, 1])

    def test_three(self):
        nums = [3]
        k = 1
        returned_value = main(nums, k)
        self.assertEqual(returned_value, [3])

    def test_four(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        k = 5
        returned_value = main(nums, k)
        self.assertEqual(returned_value, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
