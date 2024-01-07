from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        if not head.next:
            return

        # pos1
        # pos-1
        # pos2
        # pos-2

        # find middle point by using slow/fast pointers
        # pointer 1 starts at head and moved by 1
        # pointer 2 starts at second node and moved by 2

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second portion of the list
        # head of the second portion would be slow.next
        # we will store the previous node pointer in the prev variable

        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two portions

        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
