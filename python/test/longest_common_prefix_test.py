#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from longest_common_prefix import Solution  # noqa: E402


def main(strs: List[str]) -> str:
    result = Solution().longestCommonPrefix(strs)
    return result


class test(unittest.TestCase):
    def test_one(self):
        words = ["flower", "flow", "flight"]
        returned_value = main(words)
        self.assertEqual(returned_value, "fl")

    def test_two(self):
        words = ["dog", "racecar", "car"]
        returned_value = main(words)
        self.assertEqual(returned_value, "")

    def test_three(self):
        words = [""]
        returned_value = main(words)
        self.assertEqual(returned_value, "")

    def test_four(self):
        words = ["", "a"]
        returned_value = main(words)
        self.assertEqual(returned_value, "")

    def test_five(self):
        words = ["asdfasdf", "a", "asdfskdfjhskdjf'"]
        returned_value = main(words)
        self.assertEqual(returned_value, "a")

    def test_six(self):
        words = ["cane"]
        returned_value = main(words)
        self.assertEqual(returned_value, "cane")

    def test_seven(self):
        words = ["abab", "aba", "abc"]
        returned_value = main(words)
        self.assertEqual(returned_value, "ab")

    def test_eight(self):
        words = ["abab", "aba", "abc", "ab", "c", "d", "e", "a"]
        returned_value = main(words)
        self.assertEqual(returned_value, "")


if __name__ == "__main__":
    unittest.main()
