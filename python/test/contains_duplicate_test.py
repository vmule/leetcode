#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from contains_duplicate import Solution  # noqa: E402


def main(list: List[int]) -> bool:
    result = Solution().containsDuplicate(list)
    return result


class test(unittest.TestCase):
    def test_one(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        returned_value = main(nums)
        self.assertEqual(returned_value, True)

    def test_two(self):
        nums = [1, 2, 3, 4]
        returned_value = main(nums)
        self.assertEqual(returned_value, False)

    def test_three(self):
        nums = [1]
        returned_value = main(nums)
        self.assertEqual(returned_value, False)


if __name__ == "__main__":
    unittest.main()
