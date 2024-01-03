#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from container_most_water import Solution  # noqa: E402


def main(height: List[int]) -> int:
    result = Solution().maxArea(height)

    return result


class test(unittest.TestCase):
    def test_one(self):
        height = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = main(height)
        self.assertEqual(result, 30)

    def test_two(self):
        height = [100, 4, 200, 1, 3, 2]
        result = main(height)
        self.assertEqual(result, 200)

    def test_three(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = main(height)
        self.assertEqual(result, 49)

    def test_four(self):
        height = [1, 1]
        result = main(height)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
