# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = fast = head
        prev = None

        while fast and fast.next:
            
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        if fast:
            slow = slow.next

        mid = slow
        mid_reversed = prev 

        while mid_reversed and mid:
            if mid_reversed.val != mid.val:
                return False
            mid_reversed = mid_reversed.next
            mid = mid.next
        return True
