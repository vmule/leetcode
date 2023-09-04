#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from is_subsequence import Solution  # noqa: E402


def main(s: str, t: str) -> bool:
    result = Solution().isSubsequence(s, t)
    return result


class test(unittest.TestCase):
    def test_one(self):
        s = "asd"
        t = "ajhgjhghjsiuiyuiuydqqweqwe"
        returned_value = main(s, t)
        self.assertEqual(returned_value, True)

    def test_two(self):
        s = "asd"
        t = "ajhgjhghjiuiyuiuydqqwsseqwe"
        returned_value = main(s, t)
        self.assertEqual(returned_value, False)

    def test_three(self):
        s = "abc"
        t = "ahbgdc"
        returned_value = main(s, t)
        self.assertEqual(returned_value, True)

    def test_four(self):
        s = "asd"
        t = "ahbgdc"
        returned_value = main(s, t)
        self.assertEqual(returned_value, False)


if __name__ == "__main__":
    unittest.main()
