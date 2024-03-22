// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  bool isPalindrome(ListNode *head) {

    ListNode *slow = head;
    ListNode *fast = head;
    ListNode *prev = nullptr;

    while (fast && fast->next) {
      fast = fast->next->next;
      ListNode *tmp = slow->next;
      slow->next = prev;
      prev = slow;
      slow = tmp;
    }

    if (fast) {
      slow = slow->next;
    }

    ListNode *mid = slow;
    ListNode *mid_reversed = prev;

    while (mid_reversed && mid) {
      if (mid_reversed->val != mid->val) {
        return false;
      }
      mid_reversed = mid_reversed->next;
      mid = mid->next;
    }
    return true;
  }
};
