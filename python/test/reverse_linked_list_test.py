#!/usr/bin/env python3
import os
import sys
import unittest
from typing import Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.my_llist import LinkedList, ListNode  # noqa: E402
from reverse_linked_list import Solution  # noqa: E402


def reverse(head: Optional[ListNode]):
    result = Solution().reverseList(head)
    return result


def reverseRecursive(head: Optional[ListNode]):
    result = Solution().reverseListRecursive(head)
    return result


class test(unittest.TestCase):
    def test_one(self):
        test_list = [3, 2, 0, -4]
        llist = LinkedList()
        for element in test_list:
            llist.insert(element)

        result = reverse(llist.head)
        self.assertEqual(result.val, -4)

        result = reverseRecursive(llist.head)
        self.assertEqual(result.val, 3)

    def test_two(self):
        test_list = [19, 4, 5, 6, 7, 8, 9]
        llist = LinkedList()
        for element in test_list:
            llist.insert(element)

        result = reverse(llist.head)
        self.assertEqual(result.val, 9)

        result = reverseRecursive(llist.head)
        self.assertEqual(result.val, 19)


if __name__ == "__main__":
    unittest.main()
