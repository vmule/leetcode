#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from character_replacement import Solution  # noqa: E402


def main(s: str, k: int) -> int:
    result = Solution().characterReplacement(s, k)
    return result


class test(unittest.TestCase):
    def test_one(self):
        s = "AABABBA"
        k = 1
        returned_value = main(s, k)
        self.assertEqual(returned_value, 4)

    def test_two(self):
        s = "ABAB"
        k = 2
        returned_value = main(s, k)
        self.assertEqual(returned_value, 4)

    def test_three(self):
        s = "AABABBA"
        k = 2
        returned_value = main(s, k)
        self.assertEqual(returned_value, 5)


if __name__ == "__main__":
    unittest.main()
