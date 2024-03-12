from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        psum = 0
        map_psum = {}
        dummy = ListNode(0, head)
        map_psum[0] = dummy

        while head:
            psum += head.val
            if psum in map_psum:
                start = map_psum[psum]
                tmp = start
                tmp_psum = psum
                while tmp != head:
                    tmp = tmp.next
                    tmp_psum += tmp.val
                    if tmp != head:
                        del map_psum[tmp_psum]
                start.next = head.next
            else:
                map_psum[psum] = head
            head = head.next
        return dummy.next
