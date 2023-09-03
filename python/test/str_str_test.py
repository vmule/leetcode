#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from str_str import Solution  # noqa: E402


def main(haystack: str, needle: str) -> int:
    result = Solution().strStr(haystack, needle)
    return result


class test(unittest.TestCase):
    def test_one(self):
        haystack = "helloworld"
        needle = "ll"
        returned_value = main(haystack, needle)
        self.assertEqual(returned_value, 2)

    def test_two(self):
        haystack = "leetcode"
        needle = "leeto"
        returned_value = main(haystack, needle)
        self.assertEqual(returned_value, -1)

    def test_three(self):
        haystack = "asdfdfkjgdfgdfjklg"
        needle = "asdf"
        returned_value = main(haystack, needle)
        self.assertEqual(returned_value, 0)

    def test_four(self):
        haystack = "worldll"
        needle = "ll"
        returned_value = main(haystack, needle)
        self.assertEqual(returned_value, 5)


if __name__ == "__main__":
    unittest.main()
