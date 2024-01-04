from typing import Optional

from lib.my_llist import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i = 1
        while curr.next:
            i += 1
            curr = curr.next
        index = i - n

        if i == 1:
            return None

        if i == n:
            head = head.next
            return head

        curr = head
        while index > 1:
            index -= 1
            curr = curr.next
        curr.next = curr.next.next

        return head
