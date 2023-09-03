#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from reverse_words import Solution  # noqa: E402


def main(s: str) -> str:
    result = Solution().reverseWords(s)
    return result


class test(unittest.TestCase):
    def test_one(self):
        s = "Hello Calamaro"
        returned_value = main(s)
        self.assertEqual(returned_value, "Calamaro Hello")

    def test_two(self):
        s = "a b c d e f g"
        returned_value = main(s)
        self.assertEqual(returned_value, "g f e d c b a")

    def test_three(self):
        s = "the sky is blue"
        returned_value = main(s)
        self.assertEqual(returned_value, "blue is sky the")

    def test_four(self):
        s = "a"
        returned_value = main(s)
        self.assertEqual(returned_value, "a")


if __name__ == "__main__":
    unittest.main()
