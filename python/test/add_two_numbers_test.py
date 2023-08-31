#!/usr/bin/env python3
import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.my_llist import LinkedList  # noqa: E402
from add_two_numbers import Solution  # noqa: E402


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
    node = result.addTwoNumbers(node1, node2)

    result_list = []
    while node:
        result_list.append(node.val)
        node = node.next
    return result_list


class test(unittest.TestCase):
    def test_zero_array(self):
        list1 = [0]
        list2 = [0]
        expected_list = [0]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_simmetrical_array(self):
        list1 = [4, 4, 3]
        list2 = [8, 6, 4]
        expected_list = [2, 1, 8]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_simmetrical_array2(self):
        list1 = [2, 4, 3]
        list2 = [5, 6, 4]
        expected_list = [7, 0, 8]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_asymmetrical_array(self):
        list1 = [1, 9, 9, 9]
        list2 = [3, 9, 9, 9, 9, 9, 9]
        expected_list = [4, 8, 9, 9, 0, 0, 0, 1]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)

    def test_age(self):
        list1 = [4, 8, 9, 1]
        list2 = [9, 3]
        expected_list = [3, 2, 0, 2]
        returned_list = main(list1, list2)
        self.assertEqual(returned_list, expected_list)


if __name__ == "__main__":
    unittest.main()
