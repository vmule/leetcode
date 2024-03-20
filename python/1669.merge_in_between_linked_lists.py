# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        head2 = list2
        tail2 = list2
        while tail2 and tail2.next:
            tail2 = tail2.next

        i = 0
        node = ListNode(0)
        node.next = list1

        while node and node.next:
            if i == a:
                a_node = node
            if i == b + 1:
                b_node = node.next
            node = node.next
            i += 1

        a_node.next = head2
        tail2.next = b_node

        return list1
