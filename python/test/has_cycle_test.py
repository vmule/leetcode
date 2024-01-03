#!/usr/bin/env python3
import os
import sys
import unittest
from typing import Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.my_llist import LinkedList, ListNode  # noqa: E402
from has_cycle import Solution  # noqa: E402


def main(head: Optional[ListNode]):
    result = Solution().hasCycle(head)
    return result


class test(unittest.TestCase):
    def test_one(self):
        test_list = [3, 2, 0, -4]
        llist = LinkedList()
        for element in test_list:
            llist.insert(element)

        node1 = llist.head.next
        node = llist.head
        while node.next:
            node = node.next
        node.next = node1

        result = main(llist.head)
        self.assertEqual(result, True)

    def test_two(self):
        test_list = [3]
        llist = LinkedList()
        for element in test_list:
            llist.insert(element)

        result = main(llist.head)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
