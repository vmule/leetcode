#!/usr/bin/env python3
import importlib.util
import os
import sys
import unittest
from typing import List
from typing import Tuple

spec = importlib.util.spec_from_file_location(
    name="my_module",  # note that ".test" is not a valid module name
    location="../271.encode_decode_string.py",
)
my_module = importlib.util.module_from_spec(spec)
sys.modules["my_module"] = my_module
spec.loader.exec_module(my_module)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from my_module import Solution  # noqa: E402


def main(strs: List[str]) -> Tuple[str, List[str]]:
    encoded = Solution().encode(strs)
    decoded = Solution().decode(encoded)

    return encoded, decoded


class test(unittest.TestCase):
    def test_one(self):
        strs = ["lint", "code", "love", "you"]
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "4#lint4#code4#love3#you")
        self.assertEqual(decoded, strs)

    def test_two(self):
        strs = ["banana"]
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "6#banana")
        self.assertEqual(decoded, strs)

    def test_three(self):
        strs = []
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "")
        self.assertEqual(decoded, strs)

    def test_four(self):
        strs = ["bana#nana", "bananabanana"]
        encoded, decoded = main(strs)
        self.assertEqual(encoded, "9#bana#nana12#bananabanana")
        self.assertEqual(decoded, strs)


if __name__ == "__main__":
    unittest.main()
