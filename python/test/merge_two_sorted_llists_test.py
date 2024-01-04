#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.my_llist import LinkedList  # noqa: E402
from merge_two_sorted_llists import Solution  # noqa: E402


def main(list1, list2):
    llist1 = LinkedList()
    for element in list1:
        llist1.insert(element)

    llist2 = LinkedList()
    for element in list2:
        llist2.insert(element)

    node1 = llist1.head
    node2 = llist2.head
    result = Solution()
    node = result.mergeTwoLists(node1, node2)

    result_list = []
    while node:
        result_list.append(node.val)
        node = node.next
    return result_list


class test(unittest.TestCase):
    def test_one(self):
        list1 = [0]
        list2 = [0]
        expected_list = [0, 0]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_two(self):
        list1 = [2, 3, 4]
        list2 = [1, 5, 6]
        expected_list = [1, 2, 3, 4, 5, 6]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_three(self):
        list1 = []
        list2 = []
        expected_list = []
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_four(self):
        list1 = [1, 9, 9, 9]
        list2 = [9, 9, 9, 9, 9, 9]
        expected_list = [1, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)


if __name__ == "__main__":
    unittest.main()
