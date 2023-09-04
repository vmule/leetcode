#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from is_palindrome_2 import Solution  # noqa: E402


def main(s: str) -> bool:
    result = Solution().isPalindrome(s)
    return result


class test(unittest.TestCase):
    def test_one(self):
        s = "Calamaro"
        returned_value = main(s)
        self.assertEqual(returned_value, False)

    def test_two(self):
        s = "A man, a plan, a canal: Panama"
        returned_value = main(s)
        self.assertEqual(returned_value, True)

    def test_three(self):
        s = "race a car"
        returned_value = main(s)
        self.assertEqual(returned_value, False)

    def test_four(self):
        s = " "
        returned_value = main(s)
        self.assertEqual(returned_value, True)


if __name__ == "__main__":
    unittest.main()
