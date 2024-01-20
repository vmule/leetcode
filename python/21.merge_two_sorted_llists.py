from typing import Optional

from lib.my_llist import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

        return head.next
