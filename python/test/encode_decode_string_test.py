#!/usr/bin/env python3
import os
import sys
import unittest
from typing import List
from typing import Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from encode_decode_string import Solution  # noqa: E402


def main(strs: List[str]) -> Tuple[str, List[str]]:
    encoded = Solution().encode(strs)
    decoded = Solution().decode(encoded)

    return encoded, decoded


class test(unittest.TestCase):
    def test_one(self):
        strs = ["lint", "code", "love", "you"]
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "6#lint6#code6#love5#you")
        self.assertEqual(decoded, strs)

    def test_two(self):
        strs = ["banana"]
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "8#banana")
        self.assertEqual(decoded, strs)

    def test_three(self):
        strs = []
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "")
        self.assertEqual(decoded, strs)


if __name__ == "__main__":
    unittest.main()
