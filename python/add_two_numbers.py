import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from lib.my_llist import ListNode


class Solution:
    """
    https://leetcode.com/problems/add-two-numbers
    """

    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        _sum = list1.val + list2.val
        digit = _sum % 10
        carry = _sum // 10
        sum_list = ListNode(digit)
        if any((list1.next, list2.next, carry)):
            if list1.next:
                list1 = list1.next
            else:
                list1 = ListNode(0)
            if list2.next:
                list2 = list2.next
            else:
                list2 = ListNode(0)
            list1.val += carry
            sum_list.next = self.addTwoNumbers(list1, list2)
        return sum_list
