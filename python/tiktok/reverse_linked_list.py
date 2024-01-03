from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            # save next node pointer
            next = curr.next
            # change current.next pointer to previous node
            curr.next = prev
            # set previous node to current node
            prev = curr
            # move to next node
            curr = next
        head = prev

        return head
