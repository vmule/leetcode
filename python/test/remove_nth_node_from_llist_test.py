#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.my_llist import LinkedList  # noqa: E402
from remove_nth_node_from_llist import Solution  # noqa: E402


def main(my_list, n):
    llist = LinkedList()
    for element in my_list:
        llist.insert(element)

    result = Solution()
    node = result.removeNthFromEnd(llist.head, n)

    result_list = []
    while node:
        result_list.append(node.val)
        node = node.next
    return result_list


class test(unittest.TestCase):
    def test_one(self):
        llist = [0]
        n = 1
        expected_list = []
        returned_list = main(llist, n)
        self.assertEqual(returned_list, expected_list)

    def test_two(self):
        llist = [1, 2, 3, 4, 5]
        n = 2
        expected_list = [1, 2, 3, 5]
        returned_list = main(llist, n)
        self.assertEqual(returned_list, expected_list)

    def test_three(self):
        llist = [1, 2]
        n = 1
        expected_list = [1]
        returned_list = main(llist, n)
        self.assertEqual(returned_list, expected_list)


if __name__ == "__main__":
    unittest.main()
