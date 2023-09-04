#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from max_profit_2 import Solution  # noqa: E402


def main(prices: List[int]) -> int:
    result = Solution().maxProfit(prices)
    return result


class test(unittest.TestCase):
    def test_one(self):
        prices = [10, 9, 7, 4]
        returned_value = main(prices)
        self.assertEqual(returned_value, 0)

    def test_two(self):
        prices = [2, 4, 1]
        returned_value = main(prices)
        self.assertEqual(returned_value, 2)

    def test_three(self):
        prices = [1, 2, 3, 4, 5, 6]
        returned_value = main(prices)
        self.assertEqual(returned_value, 5)

    def test_four(self):
        prices = [7, 6, 4, 3, 1]
        returned_value = main(prices)
        self.assertEqual(returned_value, 0)

    def test_five(self):
        prices = [1, 6, 12, 99, 121]
        returned_value = main(prices)
        self.assertEqual(returned_value, 120)


if __name__ == "__main__":
    unittest.main()
