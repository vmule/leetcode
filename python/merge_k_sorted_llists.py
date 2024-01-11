from typing import List
from typing import Optional

from lib.my_llist import ListNode


class Solution:
    def mergeKListsBrute(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_list = []
        for element in lists:
            node = element
            while node:
                my_list.append(node.val)
                node = node.next
        my_list.sort()
        tmp = node = ListNode(0)

        for e in my_list:
            node.next = ListNode(e)
            node = node.next

        return tmp.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                print(i)
                l1 = lists[i]
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, list1, list2):
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

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return head.next
