#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from length_of_longest_substring import Solution  # noqa: E402


def main(s: str) -> int:
    # _object = Solution()
    result = Solution().lengthOfLongestSubstring(s)
    return result


class test_sum(unittest.TestCase):
    def test_one(self):
        s = "caneeee"
        returned_value = main(s)
        self.assertEqual(returned_value, 4)

    def test_two(self):
        s = "abcabcabcaaaa"
        returned_value = main(s)
        self.assertEqual(returned_value, 3)

    def test_three(self):
        s = "aloha"
        returned_value = main(s)
        self.assertEqual(returned_value, 4)

    def test_four(self):
        s = "dvdf"
        returned_value = main(s)
        self.assertEqual(returned_value, 3)

    def test_five(self):
        s = "bbbbbbbbb"
        returned_value = main(s)
        self.assertEqual(returned_value, 1)


if __name__ == "__main__":
    unittest.main()
