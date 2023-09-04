#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from can_construct import Solution  # noqa: E402


def main(ransomNote: str, magazine: str) -> bool:
    result = Solution().canConstruct(ransomNote, magazine)
    return result


class test(unittest.TestCase):
    def test_one(self):
        ramsomNote = "aaacccccc"
        magazine = "cane"
        returned_value = main(ramsomNote, magazine)
        self.assertEqual(returned_value, False)

    def test_two(self):
        ramsomNote = "aaabbb"
        magazine = "aaabbbcccddd"
        returned_value = main(ramsomNote, magazine)
        self.assertEqual(returned_value, True)

    def test_three(self):
        ramsomNote = "banana"
        magazine = "asdfabnhvngbvhvnghbdgdasdasd"
        returned_value = main(ramsomNote, magazine)
        self.assertEqual(returned_value, True)

    def test_four(self):
        ramsomNote = "b"
        magazine = "kjiueiruteirtu"
        returned_value = main(ramsomNote, magazine)
        self.assertEqual(returned_value, False)

    def test_five(self):
        ramsomNote = "aaa"
        magazine = "aaa"
        returned_value = main(ramsomNote, magazine)
        self.assertEqual(returned_value, True)


if __name__ == "__main__":
    unittest.main()
