#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from is_palindrome import Solution  # noqa: E402


def main(x: int) -> bool:
    result = Solution().isPalindrome(x)
    return result


class test(unittest.TestCase):
    def test_one(self):
        num = 47
        returned_value = main(num)
        self.assertEqual(returned_value, False)

    def test_two(self):
        num = 12233221
        returned_value = main(num)
        self.assertEqual(returned_value, True)

    def test_three(self):
        num = 1
        returned_value = main(num)
        self.assertEqual(returned_value, True)

    def test_four(self):
        num = -121
        returned_value = main(num)
        self.assertEqual(returned_value, False)


if __name__ == "__main__":
    unittest.main()
