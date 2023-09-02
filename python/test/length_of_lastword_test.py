#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from length_of_lastword import Solution  # noqa: E402


def main(s: str) -> int:
    result = Solution().lengthOfLastWord(s)
    return result


class test(unittest.TestCase):
    def test_one(self):
        s = "Hello World"
        returned_value = main(s)
        self.assertEqual(returned_value, 5)

    def test_two(self):
        s = "Dog   Cat Elephant"
        returned_value = main(s)
        self.assertEqual(returned_value, 8)

    def test_three(self):
        s = "aloha"
        returned_value = main(s)
        self.assertEqual(returned_value, 5)


if __name__ == "__main__":
    unittest.main()
